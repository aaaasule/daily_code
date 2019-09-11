# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: 内置迭代函数.py
@time: 2019/9/11 10:54
"""
from itertools import product
list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 = [2,3,4,5,6,7,8,9,10,11]
list_3 = [3,4,5,6,7,8,9,10,11,12]
# 编号迭代
for i,j in enumerate(list_1):
    print(i,j)
# 排序迭代
sorted(list_1)
print(list_1)
# 翻转迭代
reversed(list_1)
print('------')

# 并行迭代
for i,j,k in zip(list_1,list_2,list_3):
    print(i,":",j,":",k)
# print("-----------------------")
# for i,j,k in product(list_1,list_2,list_3):
#     print(i,":",j,":",k)