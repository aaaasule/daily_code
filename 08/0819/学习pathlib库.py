# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 0019 13:48
# @Author  : Zhang
# @File    : 学习pathlib库.py

import pathlib

import os

#  使用pathlib获取当前目录
values = pathlib.Path.cwd()
print(values)

# 获取上层目录的上层目录
print(os.path.dirname(os.path.dirname(os.getcwd())))  # os方法实现

print(pathlib.Path.cwd().parent.parent) # pathlib实现

# 拼接路径

# os实现
print(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),"关注","武磊","梅西"))

# pathlib实现

parts = ["关注","武磊","梅西"]
print(pathlib.Path.cwd().parent.parent.joinpath(*parts))



# PurePath

# 当前文件路径是否符合‘*py’规则的文件
print(pathlib.PurePath(__file__).match('*py'))


#   https://mp.weixin.qq.com/s/4Lf-t_8WrAPYEvfG8sKEtg

