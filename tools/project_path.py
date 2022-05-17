# -*- coding: utf-8 -*- 
# @Time : 2022/5/9 11:32 
# @Author : wxy
# @File : project_path.py


#作用：专门来读取路径的值
import os
project_path =os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#测试路径的编写(顶级目录修改的话，就会改变)
test_case_path = os.path.join(project_path,"test_data","test.xlsx")

#测试报告的路径
test_report_path =  os.path.join(project_path,"test_result","test_result.html")


#配置文件的路径
case_config_path=os.path.join(project_path,"conf","case.config")
print(case_config_path)

#日志文件的路径
case_log_path = os.path.join(project_path,"test_log.py")
