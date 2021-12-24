#!/usr/bin/python3  
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: pandas_csv_case01.py 
@time: 2021/12/24 
"""

import pandas as pd

# 三个字段 name, site, age
uid = ["1", "2", "3", "4"]
name = ["Google", "Runoob", "Taobao", "Wiki"]
time = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
addr = ["北京市", "北京市","北京市", "北京市"]

# 字典
dict = {'user_id': uid, 'name': name, 'addr': addr, 'redis_key': uid, 'time': time}

df = pd.DataFrame(dict)

# 保存 dataframe
df.to_csv('../../file/write.csv')

# 查看表
print(df)

# 表格的基本信息
# print(df.info())