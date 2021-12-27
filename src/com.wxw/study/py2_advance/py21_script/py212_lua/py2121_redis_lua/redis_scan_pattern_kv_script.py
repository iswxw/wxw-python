#!/usr/bin/python3  
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: redis_scan_pattern_kv_script.py 
@time: 2021/12/27 
"""
import sys

import redis
import pandas as pd
from optparse import OptionParser
from optparse import IndentedHelpFormatter

# [1] LUA 脚本
LUA_BATCH_READ_KV_SCRIPT = """
local keyList = {};
local result = redis.call(ARGV[1], ARGV[2], "count", ARGV[3], "MATCH", ARGV[4])
-- table.insert(keyList, result[1]);
for i, value in pairs(result[2]) do
   table.insert(keyList,value);
 end
return keyList
"""


# redis client
def redis_init(options):
    pool = redis.ConnectionPool(host=options.host, port=options.port)
    if not "1" == options.password:
        pool = redis.ConnectionPool(host=options.host, port=options.port, password=options.password)
    return redis.Redis(connection_pool=pool)


# 返回集合
imgList = []


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
parser.add_option('-O', "--out_file", action="store", help="指定输出csv文件")


# redis 读取数据
def export_file(imgList, out_file):
    result = pd.DataFrame()
    for obj in imgList:
        result = result.append({"redis_key": obj['key'], "redis_value": obj['value']}, ignore_index=True)
    result.to_csv(out_file)


def read_img_kv_from_redis(options):
    # [1] 初始化redis
    redis_client = redis_init(options)
    cmd3 = redis_client.eval(LUA_BATCH_READ_KV_SCRIPT, 1, "key1", "scan", "0", "10", "skey*")
    for key in cmd3:
        dict = {"key": str(key, encoding='utf-8'), "value": redis_client.get(key).decode()}
        imgList.append(dict)
    # [2] 数据导出到excel
    export_file(imgList, options.out_file)


# 主入口
# ./redis_scan_pattern_kv_script.py -O out.csv
if __name__ == '__main__':
    (options, args) = parser.parse_args(sys.argv[1:])
    if not options.out_file:
        parser.print_help()
        sys.exit(1)
    # 打开待读文件
    read_img_kv_from_redis(options)
