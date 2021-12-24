#!/usr/bin/python3  
# -*- coding:utf-8 _*-
""" 
@author:xiaowei
@file: pandas_excel_concurrent_process01.py
@time: 2021/12/24 
"""

import pandas as pd
import numpy as np
from multiprocessing import Pool

num_partitions = 20  # 数据分割量
num_cores = 2  # 使用逻辑核心数，注意控制，不要设太大！


def parallelize_dataframe(df, func):
    df_split = np.array_split(df, num_partitions)
    pool = Pool(num_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df


def multiply_columns(data):
    data['new_col_name'] = data.apply(
        lambda r: r['x'] * 10
    )
    return data

# 不完整
# df = parallelize_dataframe(df, multiply_columns)
