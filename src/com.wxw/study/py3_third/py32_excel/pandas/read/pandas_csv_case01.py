#!/usr/bin/python3  
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: pandas_csv_case01.py 
@time: 2021/12/24 
"""

import pandas as pd

# [1] 读 csv 文件
df = pd.read_csv('../../file/test01.csv')

# 遍历
for row in df.itertuples():
    print("读取指定行的数据：\n{0}".format(row))
    print(row.Name, row.Team, row.Salary)

print(df.head(10))