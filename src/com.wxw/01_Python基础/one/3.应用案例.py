# 1.菲比拉切数列

# 2. end的关键字
# 关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符

# a, b = 0, 1
# while b < 10:
#    # print(b)
#    print(b, end=',')
#    a, b = b, a+b  # 先计算右边表达式，然后同时赋值给左边

# print('\n');

# 3. 迭代器和生成器
#    iter()  创建迭代器对象
#    next() 输出迭代器的下一个元素

# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# for x in it:
#     print (x, end=" ")

# print('\n');

# # 导入系统模块
# import sys
# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# while True:
#     try:
#         print (next(it),end=",")
#     except StopIteration:
#         sys.exit('\n')


 # 4. 函数
 # 可写函数说明
# def sum( arg1, arg2 ):
#    # 返回2个参数的和."
#    total = arg1 + arg2
#    print ("函数内 : ", total)
#    return total
 
# # 调用sum函数
# total = sum( 10, 20 )
# print ("函数外 : ", total)

# 5. 数据结构


