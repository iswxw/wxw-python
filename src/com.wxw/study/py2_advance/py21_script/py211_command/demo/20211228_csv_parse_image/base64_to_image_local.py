#!/usr/bin/python3
# -*- coding:utf-8 _*-
"""
@author:xiaowei
@file: base64_to_image_redis.py
@time: 2021/12/22
"""
import base64
import os
import sys
import redis
import pandas as pd
from optparse import OptionParser
from optparse import IndentedHelpFormatter

num_partitions = 2  # 数据分割粒度
img_suffix = ".jpg"  # 图片后缀
img_path = "/images/"  # 图片所在包名称


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
parser.add_option('-I', "--in_file", action="store", help="指定待转换csv文件")
parser.add_option('-O', "--out_file", action="store", help="指定输出xlsx文件")


# [3] redis 客户端
def redis_client(params):
    # pool = redis.ConnectionPool(host=params.host, port=params.port, password=params.password)
    pool = redis.ConnectionPool(host=params.host, port=params.port)
    r = redis.Redis(connection_pool=pool)
    return r


# [4] 获取文件路径
def get_file_path(redis_key):
    path = os.getcwd() + img_path
    if not os.path.exists(path):
        os.makedirs(path)
    return path + redis_key + img_suffix


def base64_2_image_by_read_redis(rewards, params):
    # [1] 加载redis 配置
    r = redis_client(params)
    # [2] 解析奖励信息
    result = pd.DataFrame()
    i = 0
    # [3] 定义xlsx文件
    writer = pd.ExcelWriter(params.out_file)
    # 写数据
    for row in rewards.itertuples():
        # [4] redis 获取img key = img
        base64_str = r.get('img')
        # [5] 转换后的图片链接 上传文件返回链接
        imgdata = base64.b64decode(base64_str)
        # [6] 图片路径
        file_path = get_file_path(row.redis_key)
        file = open(file_path, 'wb')
        file.write(imgdata)
        file.close()
        # 追加数据
        result = result.append(
            {
                "用户ID": row.user_id,
                "姓名": row.name,
                "地址": row.addr,
                "图片Key": row.redis_key,
                "图片地址": file_path
            },
            ignore_index=True)
        # [5] 写入输出xlsx文件
        result.to_excel(writer, sheet_name='sheet_' + str(int(i / num_partitions)))
        i = i + 1
        if i % num_partitions == 0:
            result = result.drop(index=result.index)
    writer.save()

# command
#  - ./base64_to_image_redis.py -I in_file.csv -O test.xlsx
if __name__ == '__main__':
    (options, args) = parser.parse_args(sys.argv[1:])
    if not (options.in_file and options.out_file):
        parser.print_help()
        sys.exit(1)
    # 打开待读文件
    rewardList = pd.read_csv(options.in_file)
    base64_2_image_by_read_redis(rewardList, options)
