#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/15 22:58
# @Author  : wxw
# @Site    : https://www.bilibili.com/video/BV1R7411F7JV?p=130
# @File    : 10_生成器和迭代器.py
# @Software: PyCharm

"""
通过列表生成式(列表推导式) 我们可以直接创建一个列表，但是受内存限制，列表的容量是有限的
而且创建一个包含100万个元素的列表，不仅占用很大的存储空间
如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间就白白浪费了
所以，如果列表元素可以按照某种算法推算出来，那么我们是否可以在不断循环过程中推算出后续的元素
在Python中，中就是生成器 generator
生成器的方式：
1. 通过列表推导式
2. 借助函数 https://www.runoob.com/w3cnote/python-yield-used-analysis.html
"""
# 列表推导式 [] 方括号
list = [x * 3 for x in range(20)]
print(list)
# 生成器  () 圆括号
g = (x * 3 for x in range(10))
print(type(g))  # generator
# 获取生成器中的元素

# 方式1：通过调用__next__() 方式取得元素
print(g.__next__())  # 0
print(g.__next__())  # 3

# 方式2：next(生成器对象g) builtins 系统内置函数
print(next(g))  # 6

# 异常捕捉
while True:
    try:
        next(g)
    except:
        print("没有更多的元素了")
        break


# https://www.cnblogs.com/niuu/p/10150402.html yield 用法
# 函数中只要出现 yield关键字 就相当于 一个生成器
# yield 生成器
# 1. 定义一个函数，函数中使用yield关键字
# 2. 接收函数，接收调用的结果
# 3. 得到的结果就是生成器
# 4. 借助于 next() || __next__() 获得生成元素
def func():
    n = 0
    while True:
        n += 1
        # print(n)
        yield n


g = func()
print(next(g))

print("==============")
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
