# -*- coding:utf-8 -*-
import requests
from requests.exceptions import Timeout


class htmlDownLoader(object):
    def __init__(self):
        pass
        
    #网页下载
    def htmlDownload(self,url):
        try:
            headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
            html = requests.get(url, headers=headers).content
            return html
        except Exception:
            return '链接错误！'
    
    