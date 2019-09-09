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
                f.write(dat[0] + '\t' + 'B-ORG' + '\n')
                for i in range(1,len(dat)-1):
                    # print(i)
                    # print(dat[-1])
                    f.write(dat[i] + '\t' + 'I-ORG' +'\n')
                f.write("\n")






file_name = r"G:\下载\语料\Organization-Names-Corpus（110W）\Organization-Names-Corpus（110W）组织机构名.txt"

file_goal = r"g:\PycharmProjects\daily_code\09\0909\data_organiza.txt"

biaozhu(file_name,file_goal)

# with open(r"g:\PycharmProjects\daily_code\09\0902\data_bj_plot_b.tsv",'r',encoding='utf8') as f:
#     with open(r"g:\PycharmProjects\daily_code\09\0902\data_bj_plot_ed.tsv", 'w', encoding='utf8') as f1:
#         dats = f.readlines()
#         print(type(dats))
#         print(dats)
#         for dat in dats:
#             if dat == '\tI-LOC\n':
#                 dats.remove(dat)
#
#         for dat in dats:
#
#
#             f1.write(dat)

