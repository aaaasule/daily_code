# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: test_redis.py.py
@time: 2019/9/19 14:18
"""
import redis

conn = redis.Redis(host="127.0.0.1", port=6379, password="123456")
conn.set(1,1)

if not conn.get(1):
    print(1)
else:
    print(0)