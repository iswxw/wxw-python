#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/5 14:53
# @Author  : wxw
# @Site    : https://www.runoob.com/python/python-variable-types.html
# @File    : 2_变量类型.py
# @Software: PyCharm

# 1.Python变量赋值: 不需要类型声明,每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串
print(counter, miles, name)

# 2.多个变量赋值 Python允许你同时为多个变量赋值
a = b = c = 1
# 以为多个对象指定多个变量，两个整型对象 1 和 2 分别分配给变量 x 和 y，字符串对象 "john" 分配给变量 z。
x, y, z = 1, 2, "john"
print(a, b, c, x, y, z)

# 3,标准数据类型:Numbers（数字）/String（字符串）/List（列表）/Tuple（元组）/Dictionary（字典）
# 4.Numbers（数字）：数字数据类型用于存储数值
# (1) 查看数据类型
a=111
print(type(a))
print(isinstance(a,int))

# (2) 整型
print('除法，得到浮点数：',9/4)
print('除法，得到整数：',9//4)
print('取余：',18 % 5)
print('乘方：',2**3)

# 可以使用del语句删除一些对象的引用
# int（有符号整型）/long（长整型[也可以代表八进制和十六进制]）/float（浮点型）/complex（复数）
'''
5.String（字符串）:字符串或串(String)是由数字、字母、下划线组成的一串字符
  (1) python的字串列表有2种取值顺序:
        从左到右索引默认0开始的，最大范围是字符串长度少1
        从右到左索引默认-1开始的，最大范围是字符串开头
  (2) 字符串截取 [左闭右开]：使用 [头下标:尾下标] 来截取相应的字符串
  (3) 加号（+）是字符串连接运算符，星号（*）是重复操作
'''
str = 'Hello World!'

print(str)  # 输出完整字符串
print(str[0])  # 输出字符串中的第一个字符
print(str[2:5])  # 输出字符串中第三个至第六个之间的字符串
print(str[2:])  # 输出从第三个字符开始的字符串
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 输出连接的字符串

print(str[:-1])

'''
List（列表）
'''
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']
print(list)  # 输出完整列表
print(list[0])  # 输出列表的第一个元素
print(list[1:3])  # 输出第二个至第三个元素
print(list[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)  # 输出列表两次
print(list + tinylist)  # 打印组合的列表

'''
Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
# 元组中的元素类型也可以不相同：
'''

tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

'''
(6) 集合（set）
    由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
    基本功能是进行成员关系测试和删除重复元素。
  可以使用大括号 { } 或者 set() 函数创建集合，
  注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)  # 输出集合，重复的元素被自动去掉
# # 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# # set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素

# Dictionary（字典）
'''
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
'''

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

# 局部要声明全局变量使用 global
def test():
    global a #声明全局变量在函数中的标识
    a = 10
    print(a)

# 如果没有局部变量，默认使用全局变量
test()
