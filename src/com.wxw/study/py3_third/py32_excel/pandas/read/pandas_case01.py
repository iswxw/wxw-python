#!/usr/bin/python3  
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: pandas_case01.py
@time: 2021/12/23 
"""

import pandas as pd
# from pandas import DataFrame

"""
 DataFrame 操作方法：
    - df.itertuples() 按照行遍历
"""

# [1] 读xlsx数据
#  pandas读文档：https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas.read_excel
df = pd.read_excel('../../file/output.xlsx', index_col=0)
print(df)

# [2] 按行遍历
for row in df.itertuples():
    print("读取指定行的数据：\n{0}".format(row))
    print(row.Index, row.name, row.age)
# Pandas(Index=3, name='PHP', age=19)

# [3] 读取列


# [4] 字典打印
print(df.to_dict())
# {'name': {1: 'Java', 2: 'Go', 3: 'PHP'}, 'age': {1: 18, 2: 13, 3: 19}}
print(df.to_dict('records'))
# [{'name': 'Java', 'age': 18}, {'name': 'Go', 'age': 13}, {'name': 'PHP', 'age': 19}]
