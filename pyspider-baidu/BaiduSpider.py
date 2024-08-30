#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2017-03-01 09:14:13
# Project: baidu

from pyspider.libs.base_handler import *
import re
import time
import htmlContentPrase
import SpiderTaskMysql
import MakeUrl
import sys
import json
from urllib.request import quote
from urllib.request import pathname2url
from urllib.request import url2pathname



class Handler(BaseHandler):
    crawl_config = {
    }
    datetime = ""
    pn = 0
    
    @every(minutes=1 * 60)
    def on_start(self):
        result = SpiderTaskMysql.SelectTask()
        if result is not None:
            urls = MakeUrl.MakeUrl(result)
            for url in urls:
                self.crawl(url[0], fetch_type='js', callback=self.index_page, validate_cert=False, priority=result[2], save={'priority': result[2], 'taskid': result[0], 'date': url[1]})


    def index_page(self, response):
        #print(response.save['taskid'])
        for each in response.doc('a[href^="http"]').items():
            if re.match("http://www\.baidu\.com/link.*", each.attr.href, re.S):
                SpiderTaskMysql.InsertUrl((response.save['taskid'], each.attr.href))
                self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False, priority=response.save['priority'], save=response.save)
            if re.match(".*rsv_page=1", each.attr.href, re.S):
                self.crawl(each.attr.href, callback=self.next_page, validate_cert=False, priority=response.save['priority'], save=response.save)
     
        
    
    def next_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            if re.match("http://www\.baidu\.com/link.*", each.attr.href, re.S):
                SpiderTaskMysql.InsertUrl((response.save['taskid'], each.attr.href))
                self.crawl(each.attr.href, callback=self.detail_page, validate_cert=False, priority=response.save['priority'], save=response.save)
            if re.match(".*rsv_page=1", each.attr.href, re.S):
                self.crawl(each.attr.href, callback=self.next_page, validate_cert=False, priority=response.save['priority'], save=response.save)
                
                
    def detail_page(self, response):
        html_content = htmlContentPrase.remove_any_tag(htmlContentPrase.extract(response.text))
        datetime = time.strftime("%Y-%m-%d", time.localtime(response.save['date']))
        SpiderTaskMysql.InsertResult((response.orig_url, json.dumps({"url": response.url,"title": response.doc('title').text(),"content": html_content,"date": datetime},sort_keys=True, ensure_ascii=False)))
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            "content": html_content,
            "date": datetime,
        }
