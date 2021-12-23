#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/8 13:26
# @Author  : wxw
# @Site    : https://www.runoob.com/python/python-modules.html
# @File    : 5_模块和包.py
# @Software: PyCharm

'''
(1)Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。
        import module1[, module2[,... moduleN]]
        from modname import name1[, name2[, ... nameN]]
        from modname import *
(2)搜索路径: 当你导入一个模块，Python 解析器对模块位置的搜索顺序是：
    1、当前目录
    2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
    3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。
    模块搜索路径存储在 system 模块的 sys.path 变量中。变量里包含当前目录，PYTHONPATH和由安装过程决定的默认目录。
(3)Python中的包,包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的 Python 的应用环境。
    简单来说，包就是文件夹，但该文件夹下必须存在 __init__.py 文件, 该文件的内容可以为空。__init__.py 用于标识当前文件夹是一个包。

'''
# 导入模块
#import support
# 现在可以调用模块里包含的函数了
#support.print_func("Runoob")

'''
# 引入自定义模块 
# 文件夹 lib 包
# 文件夹里面的 sum.py:模块
'''
from lib import sum

'''
# 引入系统模块
'''
import sys
import os

print(sum.add(10,20))


