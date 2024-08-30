# -*- coding:utf-8 -*-
from htmlDownload import htmlDownLoader
from htmlparser import htmlParser
from saveDate import saveDatas
from urlManage import urlManeger
import time
from sql.v9_news import v9_news
from sql.v9_news_data import v9_news_data


data_count = 0
class mainSpider(object):
    def __init__(self):
        self.download = htmlDownLoader()
        self.parser = htmlParser()
        self.urlManage = urlManeger()
        self.save = saveDatas()
        self.v9 = v9_news()
        self.v9_data = v9_news_data()
   
    #保存一级页面数据到数据库
    def crawlSpiderSaveDBFirst(self,root_url,number,keyword):
        #lis_v9_data = []
        keyword = keyword.replace('%20','')
        global count,data_count
        lis = []
        try: 
            crawlUrl = root_url
            html = self.download.htmlDownload(crawlUrl)
            if html:
                #spider.htmlParserFirst(html, keyword, root_url)
                main_title,urls,titles,images,discriptions=self.parser.htmlParserFirst(html, keyword, crawlUrl)
                if urls is not None:
                    for j in xrange(len(urls)):
                        
                        if number == data_count:
                            print '数据已达上限！'
                            break
                        else:
                            data_count+=1
                            catid = 1
                            typeid = 0
                            title = titles[j]
                            thumb =  images[j]
                            keywords = keyword
                            discription = discriptions[j]
                            posids = 0
                            url = urls[j]
                            listorder = 0
                            status = 99
                            sysadd = 1
                            islink = 0
                            username = 'admin'
                            inputtime = time.time()
                            updatetime = time.time()
                            #v9_news_data字段
                            content = titles[j]
                            readpoint = 0
                            groupids_view = 'null'
                            paginationtype = 0
                            maxcharperpage = 10000
                            template = 'null'
                            paytype = 0
                            voteid = 0
                            relation = 'null'
                            allow_comment = 1
                            prames_v9=(data_count,catid, typeid, title,thumb,keywords, discription, posids, url, listorder, status, sysadd, islink, username, inputtime, updatetime)
                            lis.append(prames_v9)
                            #数据入库
                            self.v9_data.insertDataToV9_data(data_count,content, readpoint, groupids_view, paginationtype, maxcharperpage, template, paytype, relation, voteid, allow_comment, url)
                           
                    #数据入库
                    self.v9.insertManyDataToV9(lis)
                    new_urls = self.urlManage.getNewUrls(urls)
                else:
                    pass
            #print '共抓取到%d条数据！'%data_count
            return new_urls,data_count
        except Exception as e:
            print e       
        
    #保存二级页面数据到数据库
    def crawlSpiderSaveDbSecond(self,page,number,keyword):
        #lis_v9_data = []
        flag = True
        keyword = keyword.replace('%20','')
        global count,data_count
        while flag:
            lis = []
            try: 
                crawlUrl,old_urls= self.urlManage.getCrawlUrl()
                if crawlUrl:
                    html = self.download.htmlDownload(crawlUrl)
                    if html:
                        #spider.htmlParserSecond(html, keyword, root_url)
                        content,main_title,urls,titles=self.parser.htmlParserSecond(html, keyword, crawlUrl)
                        if urls is not None:
                            for j in xrange(len(urls)):
                                if number == data_count:
                                    print '数据已达上限！'
                                    flag = False
                                    break
                                else:
                                    data_count+=1
                                    catid = 1
                                    typeid = 0
                                    title = titles[j]
                                    thumb =  'null'
                                    keywords = keyword
                                    discription = main_title
                                    posids = 0
                                    url = urls[j]
                                    listorder = 0
                                    status = 99
                                    sysadd = 1
                                    islink = 0
                                    username = 'admin'
                                    inputtime = time.time()
                                    updatetime = time.time()
                                    #v9_news_data字段
                                    #cotent应写在循环for外
                                    content = content
                                    readpoint = 0
                                    groupids_view = 'null'
                                    paginationtype = 0
                                    maxcharperpage = 10000
                                    template = 'null'
                                    paytype = 0
                                    voteid = 0
                                    relation = 'null'
                                    allow_comment = 1
                                    prames_v9=(data_count,catid, typeid, title,thumb,keywords, discription, posids, url, listorder, status, sysadd, islink, username, inputtime, updatetime)
                                    #prames_v9_data = (content,readpoint,groupids_view,paginationtype,maxcharperpage,template,paytype,relation,voteid,allow_comment,url)
                                    lis.append(prames_v9)
                                    #lis_v9_data.append(prames_v9_data)
                                    self.v9_data.insertDataToV9_data(data_count,content, readpoint, groupids_view, paginationtype, maxcharperpage, template, paytype, relation, voteid, allow_comment, url)
                            #数据入库
                            self.v9.insertManyDataToV9(lis)
                              
                            #将新的到的urls数据加入到待爬urls中
                            self.urlManage.getNewUrls(urls)
                            
                        else:
                            pass
                    else:
                        continue 
                else:
                    break
            except Exception:
                #print e
                pass   
        return data_count               
        
             
