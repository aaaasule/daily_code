# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: 处理数据脚本升级版本.py
@time: 2019/9/4 10:15
"""

# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: 处理标注预料脚本.py
@time: 2019/9/3 16:40
"""
import re
import os


def extra_seq(file_name):
    data = ''
    with open(file_name, 'r', encoding='utf-8') as fp:
        datas = fp.readlines()
        for text in datas:
            # print('text--->', text)
            rf = re.findall("([a-z])(\d?)", text)
            # 将所有匹配到的pattern 放在一个列表中
            rfs = list()
            for i in rf:
                r = str()
                for j in list(i):
                    r += j
                rfs.append(r)
            for f in rfs:
                text = text.replace(f, '')
            # print('text--->', text)

            for t in text:
                if t not in ['[', ']', '/']:
                    data += t

    return data.replace(" ", "")


def get_file_dir(file_dir):
    file_dirs = list()
    for root, dirs, files in os.walk(file_dir):
        # print('root--->',root)
        # print('dirs-->',dirs)
        # print('files-->',files)

        # print('----------------------------')
        for i in files:
            # print(os.path.join(root,i))
            file_dirs.append(os.path.join(root, i))
        # file_dirs.append(file_path)
    return file_dirs


if __name__ == "__main__":

    # # 循环文件目录
    # file_path = list()
    # with open("data.txt",'w',encoding='utf-8') as f:
    #     for i in file_path:
    #         text = extra_seq(i)
    #         f.write(text)

    file_root_dir = r"G:\下载\people-2014\train"

    file_dirs = get_file_dir(file_dir=file_root_dir)

    with open("data_new.txt", 'w', encoding='utf-8') as f:
        for file_dir in file_dirs:
            text = extra_seq(file_dir)
            f.write(text)
