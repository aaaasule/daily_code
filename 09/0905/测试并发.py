# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: 测试并发.py
@time: 2019/9/5 10:09
"""
from multiprocessing import cpu_count
import requests
import threading
import time
import json

# 时间装饰器

def test_time(func):
    def inner():
        t1 = time.time()
        func()
        t2 = time.time()
        print("当前请求花费时间为{}".format(t2-t1))
    return inner

@test_time
def test_interface():

    url = "http://192.168.230.129:5000/"

    payload = {
        "list":["我在胜古中路1号"]
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "363fcb86-c76a-57f5-dc39-d1d9bdd05d9d"
        }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    print(response.text)



if __name__ == '__main__':
#     login()
    try:
        i = 0
        # 开启线程数目
        tasks_number = 100
        print('测试启动')
        # time1 = time.clock()
        while i < tasks_number:
            t = threading.Thread(target=test_interface())
            t.start()
            i +=1
        # time2 = time.clock()
        # times = time2 - time1
        # print(times/tasks_number)
    except Exception as e:
        print(e)
