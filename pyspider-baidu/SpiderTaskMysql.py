# -*- coding: utf-8 -*-


import mysql.connector
import datetime

class SpiderMysql:
    conn = None
    database_host = "@@@@"
    database_user = "@@@@"
    database_pwd = "@@@@"
    def __init__(self, db):
        self.conn = mysql.connector.connect(user=self.database_user, password=self.database_pwd,
                                            host=self.database_host, database=db)
        self.cursor = None
        if self.conn is not None:
            self.cursor = self.conn.cursor()


    def select(self, sql_select):
        if self.conn is None:
            return None
        self.cursor.execute(sql_select)
        return self.cursor.fetchone()

    def selectall(self, sql_select):
        if self.conn is None:
            return None
        self.cursor.execute(sql_select)
        return self.cursor.fetchall()

    def insert(self, sql_insert, data):
        #cursor = self.conn.cursor()
        self.cursor.execute(sql_insert, data)
        self.conn.commit()
        return True

    def updata(self, sql_updata, data):
        self.cursor.execute(sql_updata, data)
        self.conn.commit()
        return True

    def close(self):
        if self.conn is not None:
            self.conn.close()


def SelectTask():
    try:
        table = SpiderMysql("spider")
        result = table.select("SELECT * FROM `task` WHERE `status` = 'not start' ORDER BY priority DESC")
        table.close()
        if result is not None:
            table = SpiderMysql("spider")
            if result[3] == 0:
                table.updata("update task set status=%s where id=%s", ("starting", result[0]))
            else:
                table.updata("update task set status=%s ,start_time=%s ,end_time=%s where id=%s", ("starting", datetime.date.today(), datetime.date.today(), result[0]))
            table.close()
        else:
            table = SpiderMysql("spider")
            table.updata("update task set status=%s where lasting=%s", ("not start", 1))
            table.close()
        return result
    except mysql.connector.Error as e:
        print("{}".format(e))
        table.close()
        return None

def InsertUrl(url):
    try:
        table = SpiderMysql("spider")
        result = table.select("SELECT * FROM `url` WHERE `task_id` = %d AND `task_url` LIKE '%s'" % url)
        table.close()
        if result is None:
            table = SpiderMysql("spider")
            sql_insert = "insert into url (task_id, task_url) values (%s, %s)"
            flag = table.insert(sql_insert, url)
            table.close()
        else:
            flag = True

        if flag is True:
            return True
        else:
            return False
    except:
        table.close()
        return False

def InsertResult(result):
    try:
        table = SpiderMysql("spider")
        sql_insert = "insert into result (url, text) values (%s, %s)"
        flag = table.insert(sql_insert, result)
        table.close()
        if flag is True:
            return True
        else:
            return False
    except:
        table.close()
        return False

def SelectSiteTask():
    try:
        table = SpiderMysql("spider")
        result = table.select("SELECT * FROM `site_task` WHERE `status` = 'not start' ORDER BY priority DESC")
        table.close()
        if result is not None:
            table = SpiderMysql("spider")
            table.updata("update site_task set status=%s where id=%s", ("starting", result[0]))
            table.close()
        else:
            table = SpiderMysql("spider")
            table.updata("update site_task set status=%s where %s", ("not start", "1"))
            table.close()
        return result
    except mysql.connector.Error as e:
        print("{}".format(e))
        table.close()
        return None

def InsertSiteUrl(url):
    try:
        table = SpiderMysql("spider")
        result = table.select("SELECT * FROM `site_url` WHERE `task_id` = %d AND `task_url` LIKE '%s'" % url)
        table.close()
        if result is None:
            table = SpiderMysql("spider")
            sql_insert = "insert into site_url (task_id, task_url) values (%s, %s)"
            flag = table.insert(sql_insert, url)
            table.close()
        else:
            flag = True

        if flag is True:
            return True
        else:
            return False
    except:
        table.close()
        return False

def InsertSiteResult(result):
    try:
        table = SpiderMysql("spider")
        sql_insert = "insert into site_result (url, text) values (%s, %s)"
        flag = table.insert(sql_insert, result)
        table.close()
        if flag is True:
            return True
        else:
            return False
    except:
        table.close()
        return False
