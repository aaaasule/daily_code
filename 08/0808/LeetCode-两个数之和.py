# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 0008 16:55
# @Author  : Zhang
# @File    : LeetCode-两个数之和.py

"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例：

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

"""

def twoSum(nums,target):

    hashmap = {}
    for index,num in enumerate(nums):
        another_num = target - num
        print('hashmap1==>',hashmap)
        if another_num in hashmap:
            print('hashmap2==>',hashmap)
            return [hashmap[another_num],index]
        hashmap[num] = index
    return None

nums = [2,7,11,14]

target = 9

twoSum(nums=nums,target=target)