# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: 处理标注预料脚本.py
@time: 2019/9/3 16:40
"""
import re


def extra_seq(file_name):

    with open(file_name,'r',encoding='utf-8') as fp:
        texts = fp.readlines()
        list1 = list()
        for text in texts:

            r = re.findall("/[a-z]{0,2}", text)
            list1.extend(r)

            print(list1)
            for i in text:
                if i not in list1:
                    print(i)



if __name__ == "__main__":

    file_dir = r"G:\下载\people-2014\test\0123\c1001-24200319.txt"
    extra_seq(file_dir)