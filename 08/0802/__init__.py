# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 0002 9:06
# @Author  : Zhang
# @File    : test_redis.py.py

print('hello 0802')

# 冒泡排序
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[i] < nums[j]:
                nums[i],nums[j] = nums[j],nums[i]

# 选择排序
def select_sort(nums):
    for i in range(len(nums)-1):
        min_index = i
        for j in range(i+1,len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]


n = [8,3,5,7,9,2,4]
# bubble_sort(n)
select_sort(n)
print(n)

