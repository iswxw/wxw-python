#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/8 12:41
# @Author  : wxw
# @Site    : https://www.bilibili.com/video/BV12E411A7ZQ?p=12
# @File    : 4_函数.py
# @Software: PyCharm

"""
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
"""


# 函数的定义
def printinfo():
    print("-------------------------")
    print("     人生苦短，我用Python   ")
    print("-------------------------")


# 函数调用
printinfo()


# 定义带返回值的函数
def addNum(a, b):
    return a + b  # 通过return返回运算结果


print("addNum(10,20)=", addNum(10, 20))


# 返回多个值的函数
def divid(a, b):
    shang = a // b
    yushu = a % b
    return shang, yushu


print("divid(5,2) 商：%d, 余数：%d" % divid(5, 2))


# 打印一条线
def printOneLine():
    print("-"*30)
printOneLine()
