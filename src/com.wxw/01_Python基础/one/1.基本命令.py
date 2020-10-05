# 1. python 保留字
import keyword

print(keyword.kwlist)

# 2. 缩进确定 if_else
if True:
    print('正确')
else:
    print('失败')

# 3.数字类型、字符串
name = '魏小伟'
print(name)
print('输出第一个到倒数第二个的所有字符', name[0:-1])

print('输出从第二个开始后的所有字符', name[1:])

# 4. 导入sys 模块

import sys

print('系统路径:')
for i in sys.path:
    print(i);
