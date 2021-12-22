#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
@Author: wxw
@since: 2019-05-13 11:46:33
@lastTime: 2019-07-01 18:06:08
@LastAuthor: Do not edit
"""

import json
import sys
import optparse


if __name__ == '__main__':

    parser = optparse.OptionParser()
    parser.add_option("-i", "--input_file", help="input ks json file")
    parser.add_option("-o", "--output_file", help="output file")
    (options, args) = parser.parse_args()
    if not (options.input_file and options.output_file):
        parser.print_help()
        sys.exit(1)

    reports = json.load(open(options.input_file))

