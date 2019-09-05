# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: 重新分配预料.py
@time: 2019/9/5 9:25
"""

import random

data_dir = r"g:\PycharmProjects\daily_code\09\0904\data_m.tsv"

with open(data_dir,'r',encoding='utf-8') as fp:

    datas = fp.readlines()


    random.shuffle(datas) # 打乱有序列表 1066 * 10，比例  9 : 1 : 1   两个1 同一个文件

# print(datas)

# 把datas分成train、test、dev三个文件元素比例 9 1 1
train = datas[:1066*9]

test = datas[1066*9:-1]

dev = datas[1066*9:-1]

#将列表中元素写入tsv文件中

def write_tsv(list,file_name):
    with open(file_name,'w',encoding='utf-8') as fp:

        for text in list:
            fp.write(text)
    fp.close()


file_dir = r'g:/PycharmProjects/daily_code/09/0905/data'

write_tsv(train,file_dir + 'train.tsv')
write_tsv(test,file_dir + 'test.tsv')
write_tsv(dev,file_dir + 'dev.tsv')