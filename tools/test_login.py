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
        res = HttpRequest.http_request(item['url'],eval(item['data']),item['method'],getattr(GetCookie,'Cookie'))
        if res.cookies:
            setattr(GetData,'Cookie',res.cookies)    #利用反射存储cookie值
        try:
            self.assertEqual(item['expect'],res.json()['code'])
            TestResult='PASS'
        except AssertionError as e:
            TestResult='Failed'
            print("执行用例出错：{}".format(e))
            raise e
        finally:   #不管对错都会执行的内容
            DoExcel.write_back(test_case_path,item['sheet_name'],item['case_id']+1,str(res.json()),TestResult)
            print("获取到的结果为：{0}".format(res.json()))

    def tearDown(self):
        pass
