# -*- coding: utf-8 -*- 
# @Time : 2022/5/8 16:54
# @Author : wxy
# @File : test_login.py
import json
import unittest

from ddt import ddt,data
from tools.get_data import GetData
from tools.http_request import HttpRequest
from tools.doExecel import DoExcel
from tools.project_path import *
from tools.test_log import MyLog
from tools.doMysql import DoMysql

my_logger=MyLog()
#test_data =DoExcel.get_data(r'D:\PythonProjects\API_AUTO\test_data\test.xlsx','login')
test_data =DoExcel.get_data(test_case_path)  #需要执行的所有用例

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass

    @data(*test_data)
    def test_api(self,item):
        #登录
        #login_url="http://47.107.168.87:8080/futureloan/mvc/api/member/login"
        # login_url ="http://api.lemonban.com/futureloan/member/login"
        # login_data={"mobile_phone":"13888888888","pwd":"123456"}
        # print(type(item['data']))
        if item['data'].find('${loan_id}')!=-1:
            if getattr(GetData,'loan_id')==None:
                query_sql = 'select mamx(Id) from loan where MemberID={0}'.format(getattr(GetData,'loan_member_id'))
                loan_id = DoMysql.do_mysql(query_sql)[0][0]
                item['data']=item['data'].replace('${loan_id}',str(loan_id))
                setattr(GetData,'loan_id',loan_id)   #利用反射将loan_id保存起来
            else:
                item['data'] = item['data'].replace('${loan_id}', str(getattr(GetData,'loan_id')))

        res = HttpRequest.http_request(item['url'],eval(item['data']),item['method'],getattr(GetData,'Cookie'))
        try:
            self.assertEqual(item['expect'],res.json()['code'])
            TestResult='PASS'
        except AssertionError as e:
            TestResult='Failed'
            my_logger.info("执行用例出错：{}".format(e))
            raise e
        finally:   #不管对错都会执行的内容
            DoExcel.write_back(test_case_path,item['sheet_name'],item['case_id']+1,str(res.json()),TestResult)
            my_logger.info("获取到的结果为：{0}".format(res.json()))

    def tearDown(self):
        pass
