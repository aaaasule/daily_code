# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: 标注数据.py
@time: 2019/9/5 15:21
"""
file_name = r"g:\PycharmProjects\daily_code\09\0902\data_bj_plot.tsv"
file_name1 = r"g:\PycharmProjects\daily_code\09\0902\data_bj_plot_1.tsv"

# def biaozhu(file_name,file_goal):
with open(file_name,'r',encoding='utf-8') as fp:
    with open(file_name1,'w', encoding='utf-8') as fp1:
        dats = fp.readlines()
        for dat in dats:
            st = ""
            for j in dat:
                if j == " ":
                    j.replace(" ","")
                    con
                else:
                    st += j
                    fp1.write(st + "\n")





# biaozhu(file_name,file_goal)

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

