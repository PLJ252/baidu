#!/user/local/bin/python2.7
# -*- coding:utf-8 -*-

from spider.mainSpider import mainSpider
from sql.v9_news import v9_news
from sql.v9_news_data import v9_news_data
#from multiprocessing.dummy import Pool
import warnings

warnings.filterwarnings("ignore",".*",Warning,"sql.sqlHelper",63)

def main():
    spider = mainSpider()
    v9_new = v9_news()
    v9_data = v9_news_data()
    #先将数据库中的表清空
    v9_new.deleteAllFromV9()
    v9_data.deleteAllFromV9_data()
#     keyword = raw_input('请输入关键词:\n')
#     page = input('请输入您需要多少页的内容:\n')
#     news_number = input('请输入你想获取的数据条数:\n')
#keyword = sys.args[1]
    keyword = "MuWinter"
    page = 5
    news_number = 100
    #如果关键字中有空格，替换空格
    keyword = keyword.replace(' ','%20')
    for number in xrange(0,page*10,10):
        root_url = 'https://www.baidu.com/s?wd='+str(keyword)+'&pn='+str(number)
        new_urls,data_count = spider.crawlSpiderSaveDBFirst(root_url,news_number,keyword)
        if new_urls is None or data_count>=news_number:
            break 
        
    #爬取数据
    if data_count<=news_number:
        count = spider.crawlSpiderSaveDbSecond(page,news_number,keyword)
        print '共抓取到%d条数据！'%count
    
  
if __name__ =='__main__':
    main()
    
    
        
    
        
        
    
    
    
    
    
    
    
    
    
    
    
