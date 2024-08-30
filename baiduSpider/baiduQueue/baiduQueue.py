from queue import Queue
# global q_top

q_top = Queue()
q_page = Queue()
flag = False
def addTopUrl(bank,keyword,seasonTime):
    for page in range(1,76):
        q_top.put([bank,keyword,page,seasonTime])


def addSecondUrl(bank,keyword,title,url,seasonTime):
    q_page.put([bank,keyword,title,url,seasonTime])