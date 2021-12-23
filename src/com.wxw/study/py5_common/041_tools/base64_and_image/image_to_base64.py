#!/usr/bin/python3  
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: image_to_base64.py 
@time: 2021/12/23 
"""

import base64

# image转base64
with open("../../../../docs/img/wxw.jpeg", "rb") as f:
    # 使用base64进行加密
    base64_data = base64.b64encode(f.read())
    # print(base64_data)
    # 写成文本格式
    file = open('base64.txt', 'wt')
    file.write(base64_data.decode())
    file.close()