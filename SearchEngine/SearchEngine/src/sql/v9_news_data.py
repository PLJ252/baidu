#!/user/local/bin/python2.7
# encoding:utf-8
from sqlHelper import mySqlHelper

#对v9_python_data表进行操作
class v9_news_data(object):
    def __init__(self):
        self.__table = mySqlHelper()
    
    #查询单行
    def selectOneFromV9_data(self,newid):
        sql = 'select * from v9_news_data where id=%s'
        prames = (newid,)
        return self.__table.selectOne(sql, prames)
    
    #全部查询
    def selectAllFromV9_data(self):
        sql = 'select * from v9_news_data'
        return self.__table.selectall(sql)
    
    #插入单行
       
    def insertDataToV9_data(self,id,content,readpoint,groupids_view,paginationtype,maxcharperpage,template,paytype,relation,voteid,allow_comment,copyfrom):
        sql = 'insert into v9_news_data(id,content,readpoint,groupids_view,paginationtype,maxcharperpage,template,paytype,relation,voteid,allow_comment,copyfrom) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        prames = (id,content,readpoint,groupids_view,paginationtype,maxcharperpage,template,paytype,relation,voteid,allow_comment,copyfrom,)
        return self.__table.insert(sql, prames)
    
    #多行插入
    def insertManyDataToV9_data(self,lis):
        sql = 'insert into v9_news_data(id,content,readpoint,groupids_view,paginationtype,maxcharperpage,template,paytype,relation,voteid,allow_comment,copyfrom) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        return self.__table.insertMany(sql, lis)
    
    
    #删除单行
    def deleteFromV9_data(self,news_id):
        sql = 'delete * from v9_news_data where id=%d'
        prames = (news_id,)
        return self.__table.delete(sql, prames)
    #删除全部
    def deleteAllFromV9_data(self):
        sql = 'delete from v9_news_data'
        
        return self.__table.deleteAll(sql)
    
    
    
    