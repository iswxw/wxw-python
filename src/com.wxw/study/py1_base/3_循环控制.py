#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/5 15:27
# @Author  : wxw
# @Site    : 
# @File    : 3_循环控制.py
# @Software: PyCharm

# 1. 普通字符迭代
for letter in 'Python':  # 第一个实例
    print('当前字母 :', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print('当前水果 :', fruit)

print("Good bye!")

# 2. 通过序列索引迭代
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):  # 函数 len() 返回列表的长度，即元素的个数。 range返回一个序列的数
    print('当前水果 :', fruits[index])

print("Good bye!")

# 循环使用 else 语句
'''
for 中的语句和普通的没有区别，else 中的语句会在循环正常执行完的情况下执行（即 for 不是通过 break 跳出而中断的）
while … else 也是一样
'''
for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print(num, '是一个质数')

# while 循环
count = 0
while count < 5:
   print(count, " is  less than 5")
   count = count + 1
else:
   print(count, " is not less than 5")
