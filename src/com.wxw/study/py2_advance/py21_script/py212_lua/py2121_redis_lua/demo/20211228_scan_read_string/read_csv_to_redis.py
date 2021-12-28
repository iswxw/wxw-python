#!/usr/bin/python3  
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: read_csv_to_redis.py 
@time: 2021/12/28 
"""
import sys

import redis
import pandas as pd
from optparse import OptionParser
from optparse import IndentedHelpFormatter


# redis client
def redis_init(options):
    pool = redis.ConnectionPool(host=options.host, port=options.port)
    if not "1" == options.password:
        pool = redis.ConnectionPool(host=options.host, port=options.port, password=options.password)
    return redis.Redis(connection_pool=pool)

# [1] 格式化包装help
class NoWrapFormatter(IndentedHelpFormatter):
    def _format_text(self, text):
        "[Does not] format a text, return the text as it is."
        return text


# [2] 使用参数
parser = OptionParser(
    prog='wxw_command',
    usage="%program [OPTION]... FILE...",
    description="从redis中使用pattern读取k-v",
    version="1.0.0",
    formatter=NoWrapFormatter())
parser.add_option("-H", "--host", action="store", help="Redis主机地址IP", default="127.0.0.1")
parser.add_option("-P", "--port", action="store", help="Redis端口", default="6379")
parser.add_option('-A', "--password", action="store", help="Redis密码", default="1")
parser.add_option('-O', "--read_file", action="store", help="指定输出csv文件")


def read_csv_to_redis(options):
    redis_client = redis_init(options)
    df = pd.read_csv(options.read_file)
    for row in df.itertuples():
        redis_client.set(row.redis_key,row.redis_value)

# 主入口  ./read_csv_to_redis.py -O out.csv
if __name__ == '__main__':
    (options, args) = parser.parse_args(sys.argv[1:])
    if not options.read_file:
        parser.print_help()
        sys.exit(1)
    # 写入redis
    read_csv_to_redis(options)




