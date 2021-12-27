#!/usr/bin/python3  
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: case_register_script.py 
@time: 2021/12/27 
"""
import time
import redis


# redis client
def redis_init():
    pool = redis.ConnectionPool(host="127.0.0.1", port="6379")
    return redis.Redis(connection_pool=pool)


# [初始化redis]
r = redis_init()

lua = """
local key = KEYS[1]
local field = ARGV[1]
local timestamp_new = ARGV[2]

-- get timestamp of the key in redis
local timestamp_old = redis.call('hget', key, field)
-- if timestamp_old == nil, it means the key is not exist
if timestamp_old == nil or timestamp_old == false or timestamp_new > timestamp_old then
    redis.call('hset', key, field .. 1, timestamp_new)
    -- timestamp_new > timestamp_old
    return redis.pcall('hset', key, field, timestamp_new)
end

"""

cmd = r.register_script(lua)

cur_time = time.time()
print(cmd(keys=['current'], args=["time", cur_time]))