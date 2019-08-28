
from __future__ import print_function

import os

import sys

"""
argv 是一个保存命令行参数的普通列表
"""

def main():
    sys.argv.append(" ") # 先添加一个空格，避免索引越界的情况
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemError(filename + 'does not exists')
    elif not os.access(filename,os.R_OK): # 判断是否具有对文件的读权限
        raise SystemError(filename + ' is not accessible')
    else:
        print(filename + ' is accessible')

if __name__ == '__main__':
    main()

# print(sys.argv)