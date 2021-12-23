#!/usr/bin/python3
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: main.py 
@time: 2021/12/22 
"""

import sys
from optparse import OptionParser
from optparse import IndentedHelpFormatter


# 格式化输入的参数
class NoWrapFormatter(IndentedHelpFormatter):
    def _format_text(self, text):
        """[Does not] format a text, return the text as it is."""
        return text


# 输入参数解析
parser = OptionParser(prog='cool python',
                      usage="%prog [OPTION]... FILE...",
                      description="酷python，分享最专业的python技术",
                      version="1.1",
                      formatter=NoWrapFormatter(),
                      epilog="""\
这一段只是为了演示效果
                              """)
# 解析参数说明
parser.add_option("-n", "--name", action="store", help="姓名")
parser.add_option("-a", "--age", action="store", help="年龄")
parser.add_option('-o', "--out", action="store_true", help="是否输出")

if __name__ == '__main__':
    (options, args) = parser.parse_args(sys.argv[1:])
    # 解析所有参数
    # print((options, args))
    # 解析单个参数
    print(options.age)

"""

使用方法：
  1. 执行脚本:
   - [mac]: python3 main.py -h
   - [win10]: main.py -h

相关资料：
  1. www.coolpython.net/python_senior/project/op-optparse.html
  
"""
