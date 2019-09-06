# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: 标注数据.py
@time: 2019/9/5 15:21
"""
def biaozhu(file_name,file_goal):
    with open(file_name,'r',encoding='utf8') as fp:
        with open(file_goal,'w',encoding='utf8') as f:
            dats = fp.readlines()
            for dat in dats:
                for i in dat:
                    if dat.index(i) == 0:
                        f.write(i + '\t' + 'B-LOC' +'\n')
                    else:
                        f.write(dat[0] + '\t' + 'I-LOC' +'\n')