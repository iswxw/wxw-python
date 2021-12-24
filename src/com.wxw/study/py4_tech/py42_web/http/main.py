#!/usr/bin/python3  
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: main.py 
@time: 2021/12/24
@link: http://www.coolpython.net/python_senior/network/requests.html
"""

# [1] 发送get请求
import requests

# res = requests.get('http://www.baidu.com')
# print(res.status_code)   # 服务器响应状态码
# print(res.text)

# [2] 获取json数据
res = requests.get('https://api.github.com/events')
print(res.json())

# [3] 发送post请求
payload = {'name': '小明', 'age': '14'}
res = requests.post("http://httpbin.org/post", data=payload)
print(res.text)

