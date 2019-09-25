# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: test_redis.py.py
@time: 2019/9/19 14:18
"""

text = " 朝鲜 最高领导人 金 正 恩 1日通 过朝鲜 各大 媒体发 表201 年新年贺 词， "

for i in text:
    print("i---》",i.strip())

txt  = [x for x in text if x != " "]

print(txt)
print(len(text))
print(len(txt))