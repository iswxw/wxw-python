#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/15 23:41
# @Author  : wxw
# @Site    : https://www.bilibili.com/video/BV1R7411F7JV?p=131
# @File    : 01_斐波拉切数列.py
# @Software: PyCharm

# 斐波拉契数列
def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        # print(b)
        yield b
        a, b = b, a + b
        n += 1


g = fib(8)
print(next(g))
print(next(g))