#!/usr/bin/python3  
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: http_get.py 
@time: 2021/12/24 
"""

import requests

res = requests.get('http://www.baidu.com')
print(res.status_code)   # 服务器响应状态码
print(res.text)