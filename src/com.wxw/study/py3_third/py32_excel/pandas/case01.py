#!/usr/bin/python3
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: pandas_case01.py
@time: 2021/12/23 
"""

import pandas as pd
import json

# 使用 Python JSON 模块载入数据
with open('../file/test01.json', 'r') as f:
    data = json.loads(f.read())

df = pd.json_normalize(
    data,
    record_path=['students'],
    # 添加列
    meta=[
        'class',
        ['info', 'president'],
        ['info', 'contacts', 'tel']
    ]
)

print(df)

