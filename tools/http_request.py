# -*- coding: utf-8 -*- 
# @Time : 2022/4/26 22:24 
# @Author : wxy
# @File : http_request.py

import requests
from tools.test_log import MyLog
my_logger=MyLog()

class HttpRequest:
    @staticmethod
    def http_request(url,data,http_method,cookie=None):
        try:
            if http_method.upper()=='GET':
                res = requests.get(url,data,cookies=cookie)
            elif http_method.upper()=='POST':
                res = requests.post(url,data,cookies=cookie)
            else:
                my_logger.info("您输入的方法是不对的！")
        except Exception as e:
            my_logger.error("请求报错了,报错为：{}".format(e))
            raise e
        return res  #返回的是消息实体

# if __name__ == '__main__':
#     #注册
#     register_url = "http://192.168.0.188:8080/futureloan/member/register"
#     register_data={"mobile_phone":"13809210923","pwd":"123456"}
#     res=requests.get(register_url,register_data)
#     print(res.status_code)
#     print(res.text)
# #登录
# login_url = "http://192.168.0.188:8080/futureloan/member/login"
# login_data={"mobile_phone":"13809210923","pwd":"123456"}
# # login_res=requests.get(login_url,login_data)
# # print(login_res.status_code)
# # print(login_res.text)
# #充值
# recharge_url = "http://192.168.0.188:8080/futureloan/member/recharge"
# recharge_data={"mobile_phone":"13809210923","pwd":"123456"}
# # recharge_res=requests.get(recharge_url,recharge_data,cookies=login_res.cookies)
# # print(res.status_code)
# # print(res.text)
#
# ##为了不传递cookie,需要在一个会话中执行所有的用例
# # #
# # s=requests.session()
# # login_res = s.get(login_url,params=login_data)
# # recharge_res = s.post(recharge_url,recharge_data)
#
# register_res = HttpRequest().http_request(login_url,login_data,'get')
# recharge_res = HttpRequest().http_request(recharge_url,recharge_data,'post')
# print("充值的结果为：{}".format(recharge_res.json()))


