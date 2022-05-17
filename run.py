# -*- coding: utf-8 -*- 
# @Time : 2022/5/8 18:06 
# @Author : wxy
# @File : run.py


import unittest
import HTMLTestReportCN
from tools import project_path
from tools import test_login
from tools import test_recharge
from tools import test_http_request
from tools.test_http_request import HttpRequest

suite=unittest.TestSuite()
#suite.addTest(TestHttpRequest("test_api"))  #测试类的实例
loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_login))
# suite.addTest(loader.loadTestsFromModule(test_recharge))
suite.addTest(loader.loadTestsFromModule(test_http_request))
# suite.addTest(loader.loadTestsFromTestCase(HttpRequest))

with open(project_path.test_report_path, "wb") as file:
    runner =  HTMLTestReportCN.HTMLTestRunner(stream=file,
                                              title="测试结果",
                                              description=None,
                                              tester="wangxy")
    runner.run(suite)

# #执行用例
# runner=unittest.TextTestRunner()
# runner.run(suite)