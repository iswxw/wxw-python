#!/usr/bin/python3  
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: main.py 
@time: 2021/12/27 
"""
import time

import redis

# 自定义释放锁lua脚本
# KEYS[1] - lock name
# ARGV[1] - token
# return 1 if the lock was released, otherwise 0
LUA_RELEASE_SCRIPT = """
    return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}
    """

# redis client
def redis_init():
    pool = redis.ConnectionPool(host="127.0.0.1", port="6379")
    return redis.Redis(connection_pool=pool)


# [初始化redis]
redis_client = redis_init()

# [1] 一次性执行
cmd1 = redis_client.eval("return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}", 2, "key1", "key2", "first", "second")
print(cmd1)

# [2] 加载到内存
cmd2 = redis_client.script_load(LUA_RELEASE_SCRIPT)
res2 = redis_client.evalsha(cmd2, 2, "key1", "key2", "first", "second")
print(res2)

# [3] 注册lua脚本
cmd3 = redis_client.register_script(LUA_RELEASE_SCRIPT)
res3 = cmd3(keys=['hello'], args=['time', time.time()])
print(res3)
