#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/15 21:30
# @Author  : wxw
# @Site    : https://www.bilibili.com/video/BV1R7411F7JV?p=128
# @File    : 8_列表推导.py
# @Software: PyCharm

# 列表推导式、字典推导式、集合推导式
# 旧的列表---> 新的列表

# 1. 列表推导式: 格式：[表达式 for 变量 in 旧列表] 或者 [表达式 for 变量 in 旧列表 if 条件]

names = ['tom', 'lily', 'china', 'jpanese', 'englist']
""" 列表推导式
def func(names):
    newslist = []
    for name in names:
        if len(name) > 3:
            newslist.append(name)
    return newslist
"""
# 过滤掉长度小于或等于3的人名
result = [name for name in names if len(name) > 3]
print(result)

""" 列表推导式
# capitalize(): 字符串第一个字母大写
# title(): 
def func(names):
    newslist = []
    for name in names:
        if len(name) > 3:
            name = name.title()
            newslist.append(name)
    return newslist
"""
# 首字母大写
result = [name.capitalize() for name in names if len(name)]
print(result)


# (x,y):x= 0~5的偶数 y= 0~10 的奇数
# [(0, 1), (0, 3), (0, 5), (0, 7), (0, 9), (2, 1), (2, 3), (2, 5), (2, 7), (2, 9), (4,
# 1), (4, 3), (4, 5), (4, 7), (4, 9)]
def func():
    newlist = []
    for i in range(5):  # 偶数
        if i % 2 == 0:
            for j in range(10):
                if j % 2 != 0:
                    newlist.append((i, j))
    return newlist

x = func()
print(x)
# 下面是替代方案
list = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(list)

# 将1-100之间，能被3整除的数，组成一个新列表
# range(1,101) 默认起始值0, 返回集合左闭右开 [1,101)
list = [i for i in range(1, 101) if i % 3 == 0]
print(list)

# 矩阵
list = [[1,2,3],[4,5,6],[7,8,9],[1,3,5]]
newlist = [i[-1] for i in list]
print(newlist)


