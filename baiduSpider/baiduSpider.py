from thread.TopPage import *
from thread.SecondPage import *
import baiduQueue.baiduQueue

if __name__ == "__main__":
    addTopUrl("农行", "大数据", [1601481600, 1609344000])
    top = []
    baiduQueue.flag = False
    for i in range(1):
        t = TopPage()
        t.start()
        top.append(t)
    second = []
    for i in range(1):
        s = SecondPage()
        print("a")
        s.start()
        second.append(s)
    a = [k.join for k in top]
    baiduQueue.flag = True