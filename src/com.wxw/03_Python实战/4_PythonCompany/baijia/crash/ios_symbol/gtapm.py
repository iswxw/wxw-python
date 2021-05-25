#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import json
import os
import sys
import cgi
import optparse
import traceback
from datetime import datetime
from imp import reload

out_json = {}
bt_image_list = []
sys_image_list = [
    "/Library/PrivateFrameworks/",
    "Library/Frameworks/",
    "/usr/lib/",
]
sdk_image_list = [
    "Noah",
    "SJSDK",
    "WZZBMediaPlayer",
    "dov",
    "du",
]
app_framework = "SuperHigh.app/Frameworks"

reload(sys)
sys.setdefaultencoding('utf-8')


def is_sys_image(image_path):
    global sys_image_list
    for name in sys_image_list:
        if name in image_path:
            return True
    return False


def is_sdk_image(image_path):
    global sdk_image_list, app_framework

    # 1. 第一种策略比对SDK的名字
    image_name = os.path.basename(image_path)
    for name in sdk_image_list:
        if name == image_name:
            return True

    # 2. 第二种策略，比对存在
    # if app_framework in image_path:
    #     return True

    return False


def get_belong_img(report, addr):
    images = report.get('binaryImages', [])
    for img in images:
        if img['imageAddr'] <= addr <= (img['imageAddr'] + img['imageSize']):
            return img

    return None


def parse_backtrace(backtrace, report):
    global bt_image_list
    num = 0
    result = []
    for trace in backtrace.get('contents', []):
        try:
            pc = trace['instructionAddr']
        except:
            traceback.print_exc()
            continue

        dic = {}
        symbol_name = trace.get('symbolName', None)
        obj_name = os.path.basename(trace.get('objectName', ''))
        if obj_name not in bt_image_list:
            # 用于binaryImage去除无用的数据
            bt_image_list.append(obj_name)

        dic['obj_name'] = obj_name

        img = get_belong_img(report, pc)
        if not img:
            print("error, no img found for pc: %s" % pc)
            dic['unsymbolicated'] = '{0:<4}{1:31} 0x{2:016x}'.format(num, 'unknown', pc)
            result.append(dic)
            num += 1
            continue

        # uuid = img['uuid'].lower().replace('-', '') 
        obj_addr = img['imageAddr']
        offset = pc - obj_addr
        obj_name = os.path.basename(img['name'])

        if symbol_name == '<redacted>':
            symbol_name = ''

        dic['pc'] = '0x{0:016x}'.format(pc)
        dic['symbol_name'] = symbol_name
        dic['obj_addr'] = '0x{0:04x}'.format(obj_addr)
        dic['offset'] = offset

        result.append(dic)
        num += 1

    return result


def parse_thread(thread, report):
    result = {}
    crashed = thread.get('crashed', False)
    index = thread.get('index', -1)
    if index == -1:
        return result

    name = thread.get('name', None)
    queue = thread.get('dispatch_queue', None)
    title = ''
    if name:
        title = 'Thread {0} name:  {1}'.format(index, name)
    elif queue:
        title = 'Thread {0} name:  Dispatch queue: {1}'.format(index, queue)
    if crashed:
        title = 'Thread {0} Crashed:'.format(index)
    else:
        title = 'Thread {0}:'.format(index)

    result['title'] = title
    result['crashed'] = crashed

    if "backtrace" in thread:
        backtrace = parse_backtrace(thread['backtrace'], report)
        result['backtrace'] = backtrace
    return result


def parse_binary_images(report):
    global bt_image_list
    img_info = []

    images = report.get('binaryImages', [])
    images = sorted(images, key=lambda k: k['imageAddr'])
    for image in images:
        path = image['name']
        name = os.path.basename(path)
        if name not in bt_image_list:
            continue

        addr = image['imageAddr']
        size = image['imageSize']

        uuid = image['uuid'].lower().replace('-', '')

        is_sys = is_sys_image(path)
        is_sdk = is_sdk_image(path)

        dic = {  # 0x{0:016x}
            "addrStart": '0x{0:016x}'.format(addr),
            "addrEnd": '0x{0:016x}'.format(addr + size - 1),
            "name": name,
            "uuid": uuid,
            "isSys": is_sys,
            "isSDK": is_sdk,
        }
        img_info.append(dic)

    out_json['binaryImages'] = img_info


def parse_thread_list(report):
    result = []
    crash = report.get('crash', None)
    if not crash:
        return
    threads = crash.get('threads', [])
    for thread in threads:
        result.append(parse_thread(thread, report))

    out_json['threadsInfo'] = result


def json_parse(report):
    parse_thread_list(report)
    parse_binary_images(report)


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-i", "--input_file")
    parser.add_option("-o", "--output_file")
    (options, args) = parser.parse_args()
    if not (options.input_file and options.output_file):
        parser.print_help()
        sys.exit(1)

    report = json.load(open(options.input_file))
    fout = open(options.output_file, 'w')
    json_parse(report)
    x = type(report)
    fout.write(json.dumps(out_json, indent=4))

    fout.close()
