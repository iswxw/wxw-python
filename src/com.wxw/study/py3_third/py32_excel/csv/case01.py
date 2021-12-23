#!/usr/bin/python3  
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: pandas_case01.py
@time: 2021/12/23 
"""
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('../file/test01.csv')
    print(df.head(10))
