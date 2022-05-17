# -*- coding: utf-8 -*- 
# @Time : 2022/5/9 22:21 
# @Author : wxy
# @File : read_config.py
import configparser

class ReadConfig:

    @staticmethod
    def get_config(file_path,section,option):
        cf = configparser.ConfigParser();
        cf.read(file_path)
        return cf[section][option]

if __name__ == '__main__':
    from API_AUTO.tools.project_path import case_config_path
    print(ReadConfig.get_config(case_config_path,"MODE","mode"))