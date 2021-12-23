#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/8 13:05
# @Author  : wxw
# @Site    : 
# @File    : 0_经典案例.py
# @Software: PyCharm

# 打印一条线
def printOneLine():
    print("-" * 30)


# 根据用户输入的数组打印相应数量的线条
def printNumLine(num):
    i = 0
    while i < num:
        printOneLine()
        i += 1


# 求3个数的和
def sum3Number(a, b, c):
    return a + b + c


# printOneLine()
# printNumLine(3)
print("求三个数之和：",sum3Number(10, 20, 30))
