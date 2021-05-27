# /usr/bin/python3

# -*-coding:utf-8-*- 
# python3.8.2

import optparse
import sys
import json

out_json = {}


def main_func(lines):
    global out_json
    num = 0
    symbol_list = []
    for line in lines:
        num = num + 1
        if num > 9:
            # Symbol Table
            result = line.replace("\n", "")
            list = result.split("\t")
            length = len(list)
            if length >= 3:
                json = {
                    "offset_start": int(list[0], 16),
                    "offset_end": int(list[1], 16),
                    "symbol_result": ' '.join(list[2:])
                }
                symbol_list.append(json)
        else:
            result = line.replace(" ", "").replace(":\t", "|").replace("\n", "")
            list = result.split("|")
            if len(list) == 2:
                out_json[list[0]] = list[1]
    out_json["SymbolTable"] = symbol_list


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-i", "--input_file")
    parser.add_option("-o", "--output_file")
    (options, args) = parser.parse_args()
    if not (options.input_file and options.output_file):
        parser.print_help()
        sys.exit(1)

    f = open(options.input_file)
    lines = f.readlines()
    main_func(lines)
    fout = open(options.output_file, 'w')
    fout.write(json.dumps(out_json, indent=4))
