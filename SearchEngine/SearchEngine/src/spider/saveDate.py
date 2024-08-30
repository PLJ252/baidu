#!/user/local/bin/python2.7
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-

class saveDatas(object):
    def __init__(self):
        pass
    #保存数据到TXT文件中     
    def savedata(self,line,line1,line2,line3,line4,line5,line6):
        f = open('spiderData.txt','a')
        f.write(line)
        f.write(line1)
        f.write(line2)
        f.write(line3)
        f.write(line4)
        f.write(line5)
        f.write(line6)
        f.close()
        

        
        
    
    
    
    
    
    
    
    
    
    
    
