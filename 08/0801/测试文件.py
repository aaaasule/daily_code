# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 0001 9:06
# @Author  : Zhang
# @File    : 测试文件.py

m,n = (0,14)
print(m,n)

def get_max_len(cards,card_len):

    arr = sorted(set(cards))
    max_n,m = (0,len(arr))
    for i in range(m-1):
        n,j = (0,1)
        x = arr[i]
        if x + 1 == arr[i+1]:
            while i + j < m and x + j == arr[i + j]:
                j = j + 1
            if max_n < j:
                max_n = j
    return max_n