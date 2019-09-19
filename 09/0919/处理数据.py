# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: 处理数据.py
@time: 2019/9/19 15:26
"""

# 处理标点符号 和标错的数据

with open("g:\PycharmProjects\daily_code\09\0902\data_bj_plot_ed.tsv",'r',encoding='utf8') as f:
    dats = f.readlines()
    for i in dats:
        print(i)