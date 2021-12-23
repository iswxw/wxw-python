#!/usr/bin/python3  
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: pandas_case01.py
@time: 2021/12/23 
"""
import pandas as pd

# 依赖 openpyxl and pandas

# [1] 写入xlsx文件
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html#pandas.DataFrame.to_excel
df1 = pd.DataFrame(
    [['Java', '18'], ['Go', '13']],
    index=['1', '2'], columns=['name', 'age'])
df1.to_excel("../../file/in_file.xlsx")

# [2] 指定sheet_name
df2 = df1.copy()
with pd.ExcelWriter('../../file/in_file.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet_1')
    df2.to_excel(writer, sheet_name='Sheet_2')
