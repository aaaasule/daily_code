# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: test_redis.py.py
@time: 2019/9/25 9:34
"""

import redis
conn = redis.Redis(host="localhost",port=6379,password="123456")
conn.set("age",17)
val = conn.get("age")
print(val)