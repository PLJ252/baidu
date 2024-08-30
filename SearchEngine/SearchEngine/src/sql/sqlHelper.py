#-*-coding:utf-8-*-

import MySQLdb
import config

class mySqlHelper(object):
    def __init__(self):
        self.conn = config.conn 
    #查询单行 
    def selectOne(self,sql,prames):
        conn = MySQLdb.connect(**self.conn)
        cur = conn.cursor()
        #���ݽ�����ֵ���ʽ����
        #cur = conn.cursor(cursorclass = MySQLdb)
        cur.execute(sql,prames)
        data = cur.fetchone()
        cur.close()
        conn.close()
        return data
    
    #查询全部数据
    def selectall(self,sql):
        conn = MySQLdb.connect(**self.conn)
        cur = conn.cursor()
        #cur = conn.cursor(cursorclass = MySQLdb)
        cur.execute(sql)
        #data = cur.fetchmany(number)接受number条数据返回
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    
    #查询多条数据
    def selectmany(self,sql,prames):
        conn = MySQLdb.connect(**self.conn)
        cur = conn.cursor()
        #cur = conn.cursor(cursorclass = MySQLdb)
        cur.execute(sql,prames)
        #data = cur.fetchmany(number)接受number条数据返回
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    
    #插入数据 
    def insert(self,sql,prames):
        conn = MySQLdb.connect(**self.conn)
        cur = conn.cursor()
        recount = cur.execute(sql,prames)
        #�ɶԶ�������ִ�в���
        #recount = cur.executemany(sql,prames)
        conn.commit()
        cur.close()
        conn.close()
        return recount
    
    #插入多条数据
    def insertMany(self,sql,lis):
        conn = MySQLdb.connect(**self.conn)
        #conn.ping(True)
        cur = conn.cursor()
        #�ɶԶ�������ִ�в���
        recount = cur.executemany(sql,lis)
        conn.commit()
        cur.close()
        conn.close()
        return recount
    
    #删除数据
    def delete(self,sql,prames):
        conn = MySQLdb.connect(**self.conn)
        cur = conn.cursor()
        recount = cur.execute(sql,prames)
        conn.commit()
        cur.close()
        conn.close()
        return recount
    #删除全部数据
    def deleteAll(self,sql):
        conn = MySQLdb.connect(**self.conn)
        cur = conn.cursor()
        recount = cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
        return recount
    
    #更新数据
    def update(self,sql,prames):
        conn = MySQLdb.connect(**self.conn)
        cur = conn.cursor()
        recount = cur.execute(sql,prames)
        conn.commit()
        cur.close()
        conn.close()
        return recount        
        

