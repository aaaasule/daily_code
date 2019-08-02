# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 0002 9:06
# @Author  : Zhang
# @File    : __init__.py.py

print('hello 0802')

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[i] < nums[j]:
                nums[i],nums[j] = nums[j],nums[i]



n = [1,3,5,7,9,2,4]
bubble_sort(n)
print(n)
