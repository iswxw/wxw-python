#!/usr/bin/python3
# -*- coding:utf-8 _*-
"""
@author:xiaowei
@file: base64_to_image.py
@time: 2021/12/22
"""

import redis
import sys
from optparse import OptionParser
from optparse import IndentedHelpFormatter
import pandas as pd


# [1] 格式化包装help
class NoWrapFormatter(IndentedHelpFormatter):
    def _format_text(self, text):
        "[Does not] format a text, return the text as it is."
        return text


# [2] 使用参数
parser = OptionParser(
    prog='wxw_command',
    usage="%program [OPTION]... FILE...",
    description="根据excel的key从redis读取base64并转换为图片",
    version="1.0.0",
    formatter=NoWrapFormatter())
parser.add_option("-H", "--host", action="store", help="Redis主机地址IP", default="127.0.0.1")
parser.add_option("-P", "--port", action="store", help="Redis端口", default="6379")
parser.add_option('-A', "--password", action="store", help="Redis密码", default="321")
parser.add_option('-I', "--in_file", action="store", help="指定待转换xlsx文件")
parser.add_option('-O', "--out_file", action="store", help="指定输出xlsx文件")


# [3] redis 客户端
def redis_client(params):
    pool = redis.ConnectionPool(host=params.host, port=params.port, password=params.password)
    r = redis.Redis(connection_pool=pool)
    return r


def base64_2_image_by_read_redis(rewards, params):
    # [1] 加载redis 配置
    # r = redis_client(params)
    print(params.host, params.port, params.password)

    # [2] 解析奖励信息
    result = pd.DataFrame()
    for row in rewards.itertuples():
        print(row.Index, row.name, row.age)
        # [3] redis 读取base64 并转换为图片
        # base64_value = r.get("picData")
        # img_data = base64.b64decode(f.read())
        # [4] 转换后的图片链接 上传文件返回链接

        # 追加数据
        result = result.append({"ID": row.Index, "name": row.name, "age": row.age}, ignore_index=True)

    # [5] 写入输出excel文件
    result.to_excel(params.out_file, index=False)


# command
#  - base64_to_image.py -I in_file.xlsx -O test.xlsx
if __name__ == '__main__':
    (options, args) = parser.parse_args(sys.argv[1:])
    if not (options.in_file and options.out_file):
        parser.print_help()
        sys.exit(1)
    # 打开待读文件
    rewardList = pd.read_excel(options.in_file)
    base64_2_image_by_read_redis(rewardList, options)
