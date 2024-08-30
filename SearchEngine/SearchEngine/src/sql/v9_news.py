#!/user/local/bin/python2.7
#encoding:utf-8
from sqlHelper import mySqlHelper
#对表v9_python进行操作

class v9_news(object):
    def __init__(self):
        self.__table = mySqlHelper()
    
    #单行查询
    def selectOneFromV9(self,newid):
        sql = 'select * from v9_news where id=%s'
        prames = (newid,)
        return self.__table.selectOne(sql, prames)
    
    #查询十五条数据
    def selectFromV9For15(self,id):
        sql = 'select * from v9_news where id limit %s,15'
        prames = (id,)
        return self.__table.selectmany(sql, prames)
    
    #全部查询
    def selectAllFromV9(self):
        sql = 'select * from v9_news'
        return self.__table.selectall(sql)
    
    def selectUrlFromV9(self):
        sql = 'select url from v9_news'
        return self.__table.selectall(sql)
    
    #插入单行数据
       
    def insertDataToV9(self,new_id,catid,typeid,title,thumb,keywords,description,posids,url,listorder,status,sysadd,islink,username,inputtime,updatetime):
        sql = 'insert into v9_news(id,catid,typeid,title,keywords,description,posids,url,listorder,status,sysadd,islink,username,inputtime,updatetime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        prames = (new_id,catid,typeid,title,thumb,keywords,description,posids,url,listorder,status,sysadd,islink,username,inputtime,updatetime,)
        return self.__table.insert(sql, prames)
    
    #插入多条数据
    def insertManyDataToV9(self,lis):
        sql = 'insert into v9_news(id,catid,typeid,title,thumb,keywords,description,posids,url,listorder,status,sysadd,islink,username,inputtime,updatetime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        
        return self.__table.insertMany(sql, lis)
    
    
    #删除数据
    def deleteFromV9(self,news_id):
        sql = 'delete from v9_news where id=%s'
        prames = (news_id,)
        return self.__table.delete(sql, prames)
    #删除全部
    def deleteAllFromV9(self):
        sql = 'delete from v9_news'
        
        return self.__table.deleteAll(sql)
        
        
        
        

