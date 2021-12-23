#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: main.py 
@time: 2021/12/23 
"""

import redis

# redis 连接池
if __name__ == '__main__':
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    r = redis.Redis(connection_pool=pool)
    r.set('age', '16')
    print(r.get('age'))
    # 结果 b'16'
