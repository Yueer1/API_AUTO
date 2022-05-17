# -*- coding: utf-8 -*- 
# @Time : 2022/5/12 16:00 
# @Author : wxy
# @File : doMysql.py

import mysql.connector
from tools.read_config import ReadConfig
from tools.project_path import *


class DoMysql:
        def do_mysql(self,query_sql,state='all'):   #query_sql理解为查询语句;state=all表示有多条，为1表示一条
                db_config = eval(ReadConfig.get_config(case_config_path,'DB','db_config'))
                #创建数据库的连接
                conn = mysql.connector.connect(**db_config)
                #增加游标
                cursor = conn.cursor()
                # #sql语句
                # sql = 'select * from member where Id = "23504"'
                #执行sql
                cursor.execute(query_sql)
                #获取执行结果
                if state==1:
                        res = cursor.fetchone()   #元组，针对一条数据
                else:
                        res = cursor.fetchall()    #针对多行数据，列表嵌套元组的
                print(res)
                #关闭游标
                cursor.close()
                #关闭连接
                conn.close()
                return res

if __name__ == '__main__':
    query_sql='select * from member where Id = "23504"'
    res =DoMysql.do_mysql(query_sql,1)
    print(res)