# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 0019 9:48
# @Author  : Zhang
# @File    : itertools模块的工具函数学习.py
from itertools import product
from itertools import islice
from itertools import takewhile

list1 = [1,2,3,4,5]

list2 = [10,20,30,40,50]

# product 扁平化循环
for i,j in product(list1,list2):
    print(i,j)


# islice  循环内隔行处理 islice(seq,start,end,step)

def parse_title(file_name):

    with open(file_name,'r') as fp:
        # 设置 step=2 跳过无意义的元素
        for line in islice(fp,0,None,2):

            yield line.strip()

# 使用   takewhile  替代  break语句
# for user in takewhile(is_qualified,users):
    #