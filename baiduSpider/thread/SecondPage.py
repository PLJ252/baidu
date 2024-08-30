import threading
import time

import pymysql

from baiduQueue.baiduQueue import q_page,flag
from baiduRequest.baiduRequest import getUrl
from service.service import seasonMap

connect = pymysql.connect(host='localhost', user='root', passwd='123456', db='db1', use_unicode=1, charset='utf8')
cursor = connect.cursor()
class SecondPage(threading.Thread):
    def __init__(self):
        super().__init__()

    def insert(self,bank,keyword,title,url,seasonTime):
        sql = "INSERT IGNORE INTO baiduspider (bank,keyword,url,seasontime) VALUES('%s','%s','%s','%s')"
        data = (bank, keyword, url, seasonMap[seasonTime[0]])
        try:
            sql1 = sql % data
            cursor.execute(sql1)
        except Exception:
            print(title + "error")
        connect.commit()

    def run(self):
        while True:
            if q_page.empty():
                time.sleep(2)
            if q_page.empty() and flag:
                break
            try:
                [bank, keyword, title, href, seasonTime] = q_page.get(block=False)
                print(title)
                url, flagc = getUrl(bank, keyword, title, href)
                print(flagc)
                if flagc:
                    self.insert(bank,keyword,title,url,seasonTime)
            except Exception:
                print("secondpageerror")
                continue
