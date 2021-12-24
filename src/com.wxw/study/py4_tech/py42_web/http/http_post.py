#!/usr/bin/python3  
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: http_post.py 
@time: 2021/12/24 
"""

import requests

payload = {'name': '小明', 'age': '14'}
res = requests.post("http://httpbin.org/post", data=payload)
print(res.text)
