# coding:utf-8
"""
使用正则做域名识别
"""
import re

def check_domain(host_name):

    if re.match(r'^(?=^.{3,255}$)[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+$', host_name):
        print(host_name)
    else:
        print('no')

check_domain("26.com")
