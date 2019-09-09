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
    data = str()
    with open(file_name,'r',encoding='utf-8') as fp:
        texts = fp.readlines()
        list1 = list()
        for text in texts:

            r = re.findall("[a-z]",text)
            list1.extend(r)

            # print(list1)
            list1.extend(['/','[',']'])
            # print(list1)
            for i in text:
                if i not in list1:
                    # print(type(i))
                    data += i
    # print(type(data))

    # print(data.replace(" ",""))
    return data.replace(" ","")

def get_file_dir(file_dir):
    file_dirs = list()
    for root,dirs,files in os.walk(file_dir):
        # print('root--->',root)
        # print('dirs-->',dirs)
        # print('files-->',files)

        # print('----------------------------')
        for i in files:
            # print(os.path.join(root,i))
            file_dirs.append(os.path.join(root,i))
        # file_dirs.append(file_path)
    return file_dirs



if __name__ == "__main__":

    # # 循环文件目录
    # file_path = list()
    # with open("data_bj_plot.tsv",'w',encoding='utf-8') as f:
    #     for i in file_path:
    #         text = extra_seq(i)
    #         f.write(text)

    print('----------------------------------------------')

    file_root_dir = r"G:\下载\people-2014\train"
    file_dirs = get_file_dir(file_dir=file_root_dir)

    with open("data_bj_plot.tsv",'w',encoding='utf-8') as f:
        for file_dir in file_dirs:
            text = extra_seq(file_dir)
            f.write(text)