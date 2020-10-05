'''
学习地址： https://www.runoob.com/python3/python3-data-type.html
标准数据类型
1.Number（数字）、String（字符串）、List(列表) 、Tuple(元组)、Set(集合)、Dictionary(字典)
'''
# (1) 查看数据类型
# a=111
# print(type(a))
# print(isinstance(a,int))

# (2) 整型
# print('除法，得到浮点数：',9/4)
# print('除法，得到整数：',9//4)
# print('取余：',18 % 5)
# print('乘方：',2**3)

# (3) 字符串 索引值以 0 为开始值，-1 为从末尾的开始位置
#     字符串的截取的语法:变量[头下标:尾下标]
# str = 'Runoob'

# print (str)          # 输出字符串
# print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
# print (str[0])       # 输出字符串第一个字符
# print (str[2:5])     # 输出从第三个开始到第五个的字符
# print (str[2:])      # 输出从第三个开始的后的所有字符
# print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str) 
# print (str + "TEST") # 连接字符串

'''
(4) List (列表)
列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
列表截取的语法格式如下:
   变量[头下标:尾下标]
索引值以 0 为开始值，-1 为从末尾的开始位置。
加号 + 是列表连接运算符，星号 * 是重复操作
'''
# list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
# tinylist = [123, 'runoob']

# print (list)            # 输出完整列表
# print (list[0])         # 输出列表第一个元素
# print (list[1:3])       # 从第二个开始输出到第三个元素
# print (list[2:])        # 输出从第三个元素开始的所有元素
# print (tinylist * 2)    # 输出两次列表
# print (list + tinylist) # 连接列表

# (5) Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
# 元组中的元素类型也可以不相同：

# tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
# tinytuple = (123, 'runoob')

# print (tuple)             # 输出完整元组
# print (tuple[0])          # 输出元组的第一个元素
# print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
# print (tuple[2:])         # 输出从第三个元素开始的所有元素
# print (tinytuple * 2)     # 输出两次元组
# print (tuple + tinytuple) # 连接元组


'''
(6) 集合（set）
    由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
    基本功能是进行成员关系测试和删除重复元素。
  可以使用大括号 { } 或者 set() 函数创建集合，
  注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''
# sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
# print(sites)   # 输出集合，重复的元素被自动去掉
# # 成员测试
# if 'Runoob' in sites :
#     print('Runoob 在集合中')
# else :
#     print('Runoob 不在集合中')


# # set可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')

# print(a)
# print(a - b)     # a 和 b 的差集
# print(a | b)     # a 和 b 的并集
# print(a & b)     # a 和 b 的交集
# print(a ^ b)     # a 和 b 中不同时存在的元素

# Dictionary（字典）
'''
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
'''

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}


print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值