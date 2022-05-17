# -*- coding: utf-8 -*- 
# @Time : 2022/5/7 11:11 
# @Author : wxy
# @File : get_data.py
from tools import project_path
import pandas as pd

class GetData:
    Cookie = None
    NoRegTel=pd.read_excel(project_path.test_case_path,sheet_name="teldata").iloc[0,0]    #拿到excel中的未注册的手机号
    normal_tel=pd.read_excel(project_path.test_case_path,sheet_name="teldata").iloc[1,0]   #和tel一样，是为了从表格中读取数据
    admin_tel=pd.read_excel(project_path.test_case_path,sheet_name="teldata").iloc[2,0]
    loan_member_id=pd.read_excel(project_path.test_case_path,sheet_name="teldata").iloc[3,0]


# setattr(GetCookie,'Cookie','')    #set attribute 设置属性值
# print(hasattr(GetCookie,'Cookie'))        #has attribute  判断是否有这个属性
# # delattr(GetCookie,'Cookie')     #delete attribute  删除这个属性
# # print(hasattr(GetCookie,'Cookie'))
# print(getattr(GetCookie,'Cookie'))   #get attribute  获取属性值

# df = pd.read_excel(project_path.test_case_path,sheet_name="teldata")
# print(df.iloc[0,0])
#获取excel表格中的内容
# print(pd.read_excel(project_path.test_case_path,sheet_name="teldata").iloc[3,0])





