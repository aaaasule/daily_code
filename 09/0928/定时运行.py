# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: 定时运行.py
@time: 2019/9/28 15:44
"""
import time
from threading import Timer


def taskName(id):
    print('zhang,14', time.ctime())
    t = Timer(interval=3, function=taskName, args=(id,), kwargs=None)
    t.start()
    if id == 1:
        print(True)
    elif id == 2:
        print(False)

resp = taskName(1)

