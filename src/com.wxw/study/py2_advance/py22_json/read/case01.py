#!/usr/bin/python3  
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: pandas_excel_case01.py
@time: 2021/12/23 
"""

import pandas as pd

# 使用 Python JSON 模块载入数据
URL = 'https://static.runoob.com/download/sites.json'
df = pd.read_json(URL)
print(df)