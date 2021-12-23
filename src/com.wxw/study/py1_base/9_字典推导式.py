#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/15 22:32
# @Author  : wxw
# @Site    : 
# @File    : 9_字典推导式.py
# @Software: PyCharm

# 制造数据
dict1 = {'name': 'tom', 'salary': 5000}
dict2 = {'name': 'lucy', 'salary': 8000}
dict3 = {'name': 'jack', 'salary': 4000}
dict4 = {'name': 'lily', 'salary': 3000}
list = [dict1, dict2, dict3, dict4]  # [{},{},{}]

# if 薪资大于 5000加200，低于等于5000 加500
newlist = [{employee['name'], employee['salary'] + 200}
           if {employee['name'], employee['salary'] > 5000}
           else employee['salary'] + 500 for employee in list]
print(newlist)

# 集合推导式 {} 类似于列表推导式，只是在其基础上加了去重功能
list = [1, 2, 3, 1, 5, 2, 1, 8, 9, 8, 9, 7]
set1 = {x + 1 for x in list if x > 5}
print(set1)

# 字典推导式
newdict = {value: key for key, value in dict1.items()}
print(newdict)








