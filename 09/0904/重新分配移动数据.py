# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: 重新分配移动数据.py
@time: 2019/9/4 17:39
"""
import re

te_list = list()
with open(r"e:\no_cut_data\filtered_data.txt", 'r', encoding='utf-8') as fp:
    # with open('data_m.tsv', 'w', encoding='utf-8') as f:
        datas = fp.readlines()
        for data in datas:
            sentence = re.findall('{"sentence": "(.{0,})", "intents":', data)
            label = re.findall('"action": {"value": "(.{2})', data)
            # f.write(label[0] + '\t' + sentence[0] + '\n')
            # print(label[0])
            # print(type(label[0]))
            # print(sentence)
            # print(data)
            te_list.append(label[0])
print(set(te_list))
