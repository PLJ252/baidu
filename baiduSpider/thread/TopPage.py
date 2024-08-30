import threading
# from baiduQueue import baiduQueue
from lxml import etree
import time

from baiduQueue.baiduQueue import q_top, addSecondUrl, addTopUrl
from baiduRequest.baiduRequest import getTopRequest


class TopPage(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            if q_top.empty():
                break
            try:
                # time.sleep(1)
                bank,keyword,page,seasonTime = q_top.get(block=False)
                response = getTopRequest(bank,keyword,page,seasonTime)
                print(response)
                response.encoding = 'utf-8'
                # print(response.text)
                html = etree.HTML(response.text)
                # print(html)
                items = html.xpath('//*/h3/a')
                if len(items) == 0:
                    print("百度安全认证，缺页+1")
                print(items)
                for item in items:
                    title = ''.join(item.xpath('.//text()'))
                    href = item.xpath('./@href')[0]
                    addSecondUrl(bank,keyword,title,href,seasonTime)
                    # time.sleep(3)
                time.sleep(3)
            except Exception:
                print("TopPageError")
                continue
