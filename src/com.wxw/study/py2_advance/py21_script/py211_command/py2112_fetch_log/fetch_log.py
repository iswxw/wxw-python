#!/usr/bin/python3  
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: fetch_log.py 
@time: 2021/12/27 
"""
import os
import sys
import time

argc = sys.argv[0]
kv = dict()
kseq = []
k = ""
g = ""
datee = time.strftime("%Y%m%d")
hour = "??"

# 遍历参数
for i in range(1, len(sys.argv)):
    tag = sys.argv[i]
    if tag.startswith("--"):
        k = tag[2:]
        if k == "":
            continue
        if k not in kv:
            kv[k] = []
            kseq.append(k)
        continue
    if k not in kv:
        continue

    kv[k].append(tag)

filters = []
# 过滤参数
for k in kseq:
    if k not in kv:
        continue
    v = kv[k]
    if k == 'g':
        g = v[0]
        continue
    if k == 'date':
        datee = v[0]
        continue
    if k == 'hour':
        hour = v[0]
        continue
    v = kv[k]
    if len(v) == 0:
        continue

    if len(v) > 1:
        filters.append('grep \|' + "%s=" % (k) + '\(' + '\|'.join(v) + '\)\|')
    else:
        filters.append('grep \|' + "%s=" % (k) + v[0] + '\|')

# 取参数
shell_cmd = "pwd"
if g == "g_test":
    shell_cmd="cat test.txt  >/dev/null;"

# 执行shell命令
print(shell_cmd)
os.system(shell_cmd)
