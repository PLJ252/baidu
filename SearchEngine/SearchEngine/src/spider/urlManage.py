#!/user/local/bin/python2.7
# -*- coding:utf-8 -*-
class urlManeger(object):
    def __init__(self):
        self.new_urls = []
        self.old_urls = []
              
    #将url添加进待爬取url列表中：new_urls(待爬取url列表)，old_urls(已爬取url列表)
    def getNewUrls(self,urls):
        if urls:
            for url in urls:
                #url既不在待爬urls列表里面也不在已爬取的urls列表里面则添加进待爬取的urls列表
                self.addNewUrl(url)
        return self.new_urls
    
    def addNewUrl(self,url):
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.append(url)
            
        return url
    
    #获取待爬取的url并将其从新的url列表中删除，添加到已爬取url列表中
    def getCrawlUrl(self):
        #从链接列表头开始遍历
        try:
            if self.new_urls is not None:
                crawlUrl = self.new_urls.pop(0)
                
                self.old_urls.append(crawlUrl)
                old_urls = self.old_urls
                return crawlUrl,old_urls
        except Exception:
            return None,None
    
        
        
    
    
    
    
    
    
    
    
    
    
    
