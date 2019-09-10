# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: 处理脏数据.py
@time: 2019/9/10 10:29
"""
file_dir = 'g:/PyCharmProjects/daily_code/09/0905/data/train.tsv'

with open(file_dir,'r',encoding='utf-8') as fp:
    datas = fp.readlines()
    print(datas)
    list_labels = []
    for i in datas:
        # print(i.split('\t'))
        list_labels.append(i[0:2])

print(set(list_labels))

# train
# {'修改', '预约', '重置', '查询    首重听一下话费余额\n', '开通', '办理', '取消', '确认', '具实', '查询', '咨询'}

# test
# {'确认', '修改', '办理', '取消', '查询', '具实', '重置', '预约', '咨询', '开通'}


