# /usr/bin/python3
# -*-coding:utf-8-*- 

import os
import subprocess

# home_dir = "/Users/jinliang/Downloads/Symbols_iOS"
home_dir = os.getcwd()
sys_dir = "Symbols/System/Library/"
sys_framework_dir = os.path.join(sys_dir, "Frameworks")
sys_private_framework_dir = os.path.join(sys_dir, "PrivateFrameworks")
usr_dir = "Symbols/usr/lib"

# 存储系统版本号和固件版本号，会变化
current_sys_ver = ""
current_os_ver = ""
current_dir_name = ""

print(sys_dir, sys_framework_dir, sys_private_framework_dir)


def isFrameworkFile(file_path, file_name):
    if os.path.isdir(file_path):
        if ".framework" in file_name:
            return True
    return False


def exec_command_file(file_path):
    global current_sys_ver
    global current_os_ver
    global current_dir_name

    command = 'dwarfdump --uuid \'' + file_path + '\''
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    # print(result.stdout)
    list = result.stdout.split("\n")

    for line in list:
        if line == "":
            continue
        line_dir_list = line.split(current_dir_name)

        # 保存当前库的目录，之后拼接上前面文件名
        symbol_dir = current_dir_name + line_dir_list[1]
        line_dir_id_list = line_dir_list[0].replace("(", "").replace(")", "").split(" ")

        # 开始入库
        print("当前系统Version：", current_sys_ver, "固件Version：", current_os_ver, "UUID：", line_dir_id_list[1], "Arch：",
              line_dir_id_list[2], "库的相对路径", symbol_dir)
        print("-----------------------------------------------------")
        return


def frameworkFileTraverse(dir):
    print("当前路径" + dir)
    for fi in os.listdir(dir):
        fi_dir = os.path.join(dir, fi)
        if isFrameworkFile(fi_dir, fi):
            # 进入文件夹遍历，如果是文件，做uuid提取
            for fi_sec in os.listdir(fi_dir):
                sec_dir = os.path.join(fi_dir, fi_sec)
                if os.path.isfile(sec_dir) and not ("." in fi_sec):
                    # 是framework的二进制文件  
                    exec_command_file(sec_dir)


def dylibFileTraverse(dir):
    for fi in os.listdir(dir):
        fi_dir = os.path.join(dir, fi)
        if os.path.isfile(fi_dir) and (".dylib" in fi_dir):
            # .dylib文件解析
            exec_command_file(fi_dir)
        elif os.path.isdir(fi_dir):
            # 文件夹，继续遍历
            dylibFileTraverse(fi_dir)


def getVersion(dir_name):
    dir_name_new = dir_name.replace(" (", " ").replace("(", " ").replace(")", "")
    name_list = dir_name_new.split(" ")
    return name_list


# 处理符号表目录
def dealwithSymbolDir(dir_path, dir_name):
    global current_sys_ver
    global current_os_ver
    global current_dir_name
    # 处理名字
    ver_list = getVersion(dir_name)
    current_sys_ver = ver_list[0]
    current_os_ver = ver_list[1]
    current_dir_name = dir_name

    # 处理地址
    # print("dealwithSymbolDir,处理地址；", dir_path)
    dw_system_framework_dir = os.path.join(dir_path, sys_framework_dir)
    dw_system_private_framework_dir = os.path.join(dir_path, sys_private_framework_dir)
    dw_usr_dylib_dir = os.path.join(dir_path, usr_dir)
    # print("dir_name"+dir_name)
    frameworkFileTraverse(dw_system_framework_dir)
    frameworkFileTraverse(dw_system_private_framework_dir)

    dylibFileTraverse(dw_usr_dylib_dir)


# main函数
if __name__ == '__main__':
    files = os.listdir(home_dir)
    for fi in files:
        fi_dir = os.path.join(home_dir, fi)
        if os.path.isdir(fi_dir):
            if "vscode" in fi_dir:
                continue
            dealwithSymbolDir(fi_dir, fi)

# print(file_name)
