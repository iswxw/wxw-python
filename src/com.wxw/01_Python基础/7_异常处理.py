#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/8 14:09
# @Author  : wxw
# @Site    : https://www.runoob.com/python/python-exceptions.html
# @File    : 7_异常处理.py
# @Software: PyCharm

try:
    fh = open("F:\\Study_GO\\Study_Project\\python\\wxw-python\\doc\\exception.txt", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()

# 测试异常 打开一个不存在的文件
try:
    fh = open("F:\\Study_GO\\Study_Project\\python\\wxw-python\\doc\\error.txt", "r")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:  # 这里就没有打开，所以不需要关闭
    print("Error: 没有找到文件或读取文件失败")
    pass  # 占位符，什么都不做
else:
    print("内容写入文件成功")
    fh.close()

try:
    fh = open("testfile", "r")
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print("关闭文件")
        fh.close()
except IOError: # 异常，则文件根本没有打开，所以不需要关闭
    print("Error: 没有找到文件或读取文件失败")