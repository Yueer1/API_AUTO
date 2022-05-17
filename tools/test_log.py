# -*- coding: utf-8 -*- 
# @Time : 2022/5/10 20:34 
# @Author : wxy
# @File : test_log.py

import logging
from tools.project_path import case_log_path
#logger 收集日志  debug info error
#handdler  输出日志的渠道 指定的文件还是控制台输出，不指定的话默认为控制台

#不给收集器，收集器的名字就是 root
# logging.debug("这是报错信息呀!")
# logging.info("这是代码的基本信息")
# logging.warning("警告呀")
# logging.error("错误信息呀")
# logging.critical("躺着舒服-")

class MyLog:
    def my_log(self,level,msg):
        #定义一个日志收集器 my_logger
        my_logger = logging.getLogger("pythontest")
        #设置级别,不设置默认为warning以上的
        my_logger.setLevel('DEBUG')
        #设置输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')
        #创建一个输出渠道
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(formatter)
        #设置输出的渠道文件等
        fh = logging.FileHandler(case_log_path, encoding='UTF-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        #收集的和输出的对接起来--两者对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        #收集日志
        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        elif level=='CRITICAL':
            my_logger.critical(msg)

        # 关闭渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log('DEBUG',msg)
    def info(self,msg):
        self.my_log('INFO',msg)
    def error(self,msg):
        self.my_log('ERROR',msg)

if __name__ == '__main__':
    MyLog().my_log('ERROR','萌萌哒123')

