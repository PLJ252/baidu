#!/user/local/bin/python2.7
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup as bs
from urlparse import urljoin
import re
from lxml.html.clean import Cleaner

class htmlParser(object):
    
    def __init__(self):
        pass
    #二级页面网页解析，根据一级页面爬取的url获取数据
    def htmlParserSecond(self,html,keyword,url):
        urls=[]
        titles=[]
        content = ''
        if html:
            try:
                soup = bs(html.decode('utf-8').encode('utf-8'),'lxml')
                main_title = soup.title.get_text()
                cleaner = Cleaner(style = True,scripts=True,page_structure=False,safe_attrs_only=False)
                content = cleaner.clean_html(html.decode('utf-8')).encode('utf-8')
                datas = soup.find_all('a') 
                #main_content = content.insert(0,content_title)
                
                for data in datas:
                    title = data.get_text().encode('utf-8')
                    #匹配含有图片的标题
                    if keyword in title:
                        m = re.match(r'.*(\d+张)',title)
                        if ('视频' in title)or('电影' in title)or('音乐' in title)or('MV' in title)or('图片' in title)or('写真' in title)or m:
                            pass
                        #补全url
                        else:
                            url = urljoin(url, data.get('href'))
                            if re.match(r'https://baike.baidu.com/pic/.*',url):
                                pass
                            else:
                                fina_url = url
                                fina_title = title
                            #本页数据去重
                                if fina_url in urls or fina_title in titles:
                                    pass
                                else:
                                    #print url,title
                                    urls.append(fina_url)
                                    titles.append(fina_title)
                return content,main_title,urls,titles
            except Exception:
                return '此链接无数据！'
        else:
            return '链接所得数据为空！'
        
    #一级页面网页解析,根据入口url获取数据
    def htmlParserFirst(self,html,keyword,base_url):  
        urls = []
        titles = []
        images = []
        discriptions = []
        #global urls,titles,images,discriptions
        #soup = bs(html,'html.parser')
        #使用lxml解析器解析网页效率更高
        soup = bs(html,'lxml')
        main_title = soup.title.get_text()
        #正则表达式来匹配以result开头的class      
        datas = soup.find('div',id='content_left').find_all('div',class_ =re.compile('^result*'))
        for data in datas:
            title = data.find('h3').find('a').get_text().encode('utf-8')
            href = data.find('h3').find('a').get('href')
            if data.find('img'):
                image_href = data.find('img').get('src')
            else:
                image_href = 'null'
            if data.find('div',class_='c-abstract'):
                discription = data.find('div',class_='c-abstract').get_text()
            else:
                discription = 'null'
                
            if keyword in title:
                #过滤不必要的数据
                if('视频' in title)or('电影' in title)or('音乐' in title)or('图片' in title)or('MV' in title):
                    pass
                else:
                #补全url
                    url = urljoin(base_url,href)
                    fina_title = title
                    #title = data.get_text()
                    #
                    if url in urls or fina_title in titles:
                        pass
                    else:
                        #print url,title
                        urls.append(url)
                        titles.append(fina_title)
                        images.append(image_href)
                        discriptions.append(discription)     
        return main_title,urls,titles,images,discriptions
            
        
        
    
    
    
    
    
    
    
    
    
    
    
