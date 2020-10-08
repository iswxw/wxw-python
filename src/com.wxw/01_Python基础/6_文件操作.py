#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/8 13:20
# @Author  : wxw
# @Site    : https://www.runoob.com/python/python-files-io.html
# @Site    : https://www.bilibili.com/video/BV12E411A7ZQ?p=13
# @File    : 6_文件操作.py
# @Software: PyCharm

"""
# 打开一个文件-W模式（写模式）,文件不存在就信件
fo = open("F:\\Study_GO\\Study_Project\\python\\wxw-python\\doc\\foo.txt", "w")
print("文件名: ", fo.name)
fo.write("hello world,i am here!")  # 将字符串写入文件中
print("文件访问模式：", fo.mode)
# 关闭打开的文件
fo.close()
"""

rd = open("F:\\Study_GO\\Study_Project\\python\\wxw-python\\doc\\foo.txt", "r")
# print(rd.read(5)) # 读指定的字符，开始时定位在文件头
# print(rd.read()) # 读取一行
# print(rd.readline()) # 读取一行

# print(rd.readlines()) # 读取全文列表
# 文件遍历
content = rd.readlines()
i = 1
for temp in content:
    print("%d:%s" % (i, temp))
    i += 1
print("文件访问模式：", rd.mode)
rd.close()  # 关闭打开的文件

# 文件 os模块
import os

print("获取当前路径：", os.getcwd())
print("登录用户：", os.getlogin())
