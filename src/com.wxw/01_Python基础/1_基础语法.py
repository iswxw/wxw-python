#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/5 14:35
# @Author  : wxw
# @Site    : https://www.runoob.com/python/python-basic-syntax.html
# @File    : 1_基础语法.py
# @Software: PyCharm

# 1. Python 标识符
# 英文、数字以及下划线(_)，但不能以数字开头，区分大小写
# 以单下划线开头 _foo 的代表不能直接访问的类属性、以双下划线开头的 __foo 代表类的私有成员

# 2. python 保留字符
# 3. 缩进代替{}
if True:
    print("缩进代替{}:", "True")
else:
    print("False")

# 4.多行语句
total = 'item_one_' + \
        'item_two_' + \
        'item_three'
print("多行语句:", total)

# 5.Python 引号 引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串
# 6.python中单行注释采用 # 开头。python 中多行注释使用三个单引号(''')或三个双引号(""")。
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

# 7.Python空行:空行分隔，表示一段新的代码的开