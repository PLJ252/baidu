require 'socket'
require 'nokogiri'
require 'mysql'

$host = 'www.baidu.com'
$port = 80
$keywords = []
$results = []
$count = 0
$mutex = Mutex.new
$total = $*[1].nil? ? 100000 : $*[1].to_i
$keywords << ($*[0] || "eLong").downcase

def baidu_search_collection(keyword, count)
  if keyword.nil?
    $count = $total
    puts "\n302\n\n"
    return
  end
  return if count > $total
  socket = TCPSocket.open($host, $port)
  print "Search #{(count + 1).to_s.rjust(6)} : #{keyword}\n"
  path = "/s?wd=#{keyword.gsub(' ','%20')}"
  request = "GET #{path} HTTP/1.0\r\n\r\n"
  socket.print(request)
  response = socket.read
  headers, body = response.split("\r\n\r\n", 2)
  return if body.nil?
  body.force_encoding("UTF-8")
  doc = Nokogiri::HTML(body)
  index = 0
  results = []
  keywords = []
  doc.css('.c-container').each do |div|
    if div.css('.t a').any?
      if div[:mu].nil?
        url = div.css('.g').any? ? div.css('.g').first.content.split.first : "null"
      else
        url = div[:mu]
      end
      results << { count: count + 1, keyword: keyword, number: index += 1, title: div.css('.t a').first.content, url: url, created_at: Time.now.to_s }
    end
  end
  socket.close
  doc.css('#rs th a').each do |rs|
    keywords << rs.content.downcase unless $keywords.include?(rs.content.downcase)
  end

  $mutex.lock
    results.each { |result| $results << result }
    keywords.each { |keyword| $keywords << keyword }
  $mutex.unlock
end

dbh = DBI.connect("DBI:Mysql:mysql:localhost", "root", "root")
dbh.do("drop table if exists results")
dbh.do("create table results(id integer PRIMARY KEY autoincrement, count integer, keyword varchar, number integer, title varchar, url varchar, created_at varchar)" )
dbh.disconnect if dbh 

puts

baidu_search_collection($keywords[$count], $count)

while $count < $total
  threads = []
  5.times do
    break if $count >= $total
    threads << Thread.new do
      baidu_search_collection($keywords[$count += 1], $count)
    end
  end
  threads.each do |t|
    t.join(5)
  end
  sleep 8
  if $count.even?
    if $results.count.eql?(0)
      $count = $total
      puts "\n302\n\n"
    else
      puts "\nSave #{$results.count} records to list.db/results\n\n"
	  dbh=DBI.connect("DBI:Mysql:test:localhost", "root", "root")
      $results.each do |result|
		dbh.do("insert into results(count, keyword, number, title, url, created_at) values(?, ?, ?, ?, ?, ?)", result[:count], result[:keyword], result[:number], result[:title], result[:url], result[:created_at] )
      end
      dbh.disconnect if dbh 
      $results.clear
    end
  end
end
