# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: 二次处理.py
@time: 2019/9/4 9:13
"""
import re

with open(r"G:\PycharmProjects\daily_code\09\0904\data_new.txt",'r',encoding='utf-8') as fp:
    datas = fp.readlines()
    dates = ['年','月','日','时','分','秒']
    # new_datas = list()
    with open(r"G:\PycharmProjects\daily_code\09\0904\data_goal.txt",'w',encoding='utf-8') as f:
        for i in datas:
            # print(i)
            if re.findall("([0-9]{1,4})(['年','月','日','时','分','秒'])",i):
                # new_datas.append(i)
                f.write(i)

