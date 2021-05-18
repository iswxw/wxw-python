#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 12:27
# @Author  : wxw
# @Site    : 对crash log 解析优化
# @File    : crash-parser.py

import json
import os
import sys
import cgi
import optparse
import traceback

CPU_TYPE_ARM = 12
CPU_ARCH_ABI64 = 0x01000000
CPU_TYPE_ARM64 = CPU_TYPE_ARM | CPU_ARCH_ABI64
CPU_TYPE_X86 = 7
CPU_TYPE_X86_64 = CPU_TYPE_X86 | CPU_ARCH_ABI64

CPU_SUBTYPE_ARM_V6 = 6
CPU_SUBTYPE_ARM_V7 = 9
CPU_SUBTYPE_ARM_V7F = 10
CPU_SUBTYPE_ARM_V7S = 11
CPU_SUBTYPE_ARM_V7K = 12
CPU_SUBTYPE_ARM_V6M = 14
CPU_SUBTYPE_ARM_V7M = 15
CPU_SUBTYPE_ARM_V7EM = 16
CPU_SUBTYPE_ARM_V8 = 13

CPU_ARM_TYPES = {
    CPU_SUBTYPE_ARM_V6: 'armv6',
    CPU_SUBTYPE_ARM_V7: 'armv7',
    CPU_SUBTYPE_ARM_V7F: 'armv7f',
    CPU_SUBTYPE_ARM_V7S: 'armv7s',
    CPU_SUBTYPE_ARM_V7K: 'armv7k',
    CPU_SUBTYPE_ARM_V6M: 'armv6m',
    CPU_SUBTYPE_ARM_V7M: 'armv7m',
    CPU_SUBTYPE_ARM_V7EM: 'armv7em',
    CPU_SUBTYPE_ARM_V8: 'armv8',
}


# cpu架构
def get_detail_cpu_arch(major, minor):
    if major == CPU_TYPE_ARM:
        return CPU_ARM_TYPES.get(minor, 'arm')
    elif major == CPU_TYPE_ARM64:
        return 'arm64'
    elif major == CPU_TYPE_X86:
        return 'i386'
    elif major == CPU_TYPE_X86_64:
        return 'x86_64'
    return 'unknown({0},{1})'.format(major, minor)


# Get report information from report
def get_report_info(report):
    return report.get('report', None)


# 二进制镜像信息
def get_binary_img_info(report):
    # key: name, value: uuid
    img_info = {}

    images = report.get('binaryImages', [])
    for image in images:
        name = os.path.basename(image["name"])
        uuid = image['uuid'].lower().replace('-', '')

        if name not in img_info:
            img_info[str(name)] = str(uuid)

    return img_info


# Get crash information from report
def get_crash_info(report):
    return report.get('crash', None)


# 获取镜像地址
def get_belong_img(report, addr):
    images = report.get('binaryImages', [])
    for img in images:
        if img['imageAddr'] <= addr <= (img['imageAddr'] + img['imageSize']):
            return img
    return None


# 解析堆栈信息
def parse_backtrace(report, backtrace):
    result = []
    for trace in backtrace.get('contents', []):
        try:
            pc = trace['instructionAddr']
        except:
            traceback.print_exc()
            continue
        img = get_belong_img(report, pc)
        if not img:
            print "error, no img found for pc: %s" % pc
            result.append('{{0:31} 0x{1:016x}'.format('unknown', pc))
            continue
        obj_addr = img['imageAddr']
        preamble = '0x{0:016x}'.format(pc)
        unsymbolicated = '0x{0:04x}'.format(obj_addr)
        # result.append({'imageAddr': preamble, 'objStartAddr': unsymbolicated})
        result.append('{0} {1}'.format(preamble, unsymbolicated))
    return result


# 解析线程信息
def parse_thread_info(thread, report):
    result = []
    crashed = thread.get('crashed', False)
    index = thread.get('index', -1)
    if index == -1:
        return result
    name = thread.get('name', None)
    queue = thread.get('dispatch_queue', None)

    if name:
        result.append('ThreadName:{1}'.format(index, name))
    elif queue:
        result.append('ThreadName:  Dispatch queue: {1}'.format(index, queue))
    if crashed:
        result.append('ThreadCrashed:'.format(index))

    if "backtrace" in thread:
        backtrace = parse_backtrace(report, thread['backtrace'])
        result += backtrace
    return result


# 解析线程信息
def parse_thread_list(report):
    crash = get_crash_info(report)
    if not crash:
        return []
        # print dump_json( crash)
    threads = crash['threads']

    result = []
    for thread in threads:
        result.append('')
        result += parse_thread_info(thread, report)
    return result


# 从系统信息中获取系统名称
def get_system_info(report):
    # Get system information from report
    return report.get('system', None)


# app 名称  问题1
def get_app_name(report):
    system = get_system_info(report)
    return system.get('CFBundleExecutable', 'unknown')


# 解析json 文件并输出到指定文件
def ks_json_2_apple(report, fout):
    global IMG_INFO_MAP, APP_NAME
    # 二进制星系
    IMG_INFO_MAP = get_binary_img_info(report)
    # app名称
    APP_NAME = get_app_name(report)

    # 线程信息
    threads = parse_thread_list(report)
    for line in threads:
        line = cgi.escape(line)
        fout.write(line + '\n')


if __name__ == '__main__':
    # 读取控制台参数
    parser = optparse.OptionParser()
    parser.add_option("-i", "--input_file", help="input ks json file")
    parser.add_option("-o", "--output_file", help="output file")
    (options, args) = parser.parse_args()
    if not (options.input_file and options.output_file):
        parser.print_help()
        sys.exit(1)
    # 打开文件
    reports = json.load(open(options.input_file))

    # 打开写入文件
    fout = open(options.output_file, 'w')
    ks_json_2_apple(reports, fout)
    fout.close()
