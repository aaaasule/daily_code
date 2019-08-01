# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 0001 9:06
# @Author  : Zhang
# @File    : 测试文件.py

name = "高兴"
tem_n = "很高兴认识你，{}先生"
tem_name = tem_n.format(name)
tem_name = tem_name + ' '
guolv = []
for i in tem_n:
    if i in name:
        guolv.append(i)

for n in tem_name:
    if n == name[0] and n not in guolv:
        print(n + '   B-PER\n')
    elif n in str(name) and n not in guolv:
        print(n + '   I-PER\n')

    else:
        if n != ' ':
            print(n + '   O\n')
        elif n == ' ':
            print(n + '   \n')