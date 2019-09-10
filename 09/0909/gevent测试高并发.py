# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: gevent测试高并发.py
@time: 2019/9/9 14:50
"""
import time
import json
import random
from urllib.error import URLError
from urllib import request
import http.client
import requests
import gevent
from gevent import monkey

# # 补丁
# monkey.patch_all()
#
# #** 请求URL **
# url = 'http://127.0.0.1:8000/insert'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
#            }


# def make_data(num):
#     """制造请求数据"""
#     data = {
#         "id": num,
#         "name": "test" + num,
#     }
#     return data


def run():

    url = "http://192.168.230.129:5000/"

    payload = {
              "list":["我在胜古中路1号"]
            }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "44bdf9df-2992-3a8b-7818-2752789d88fd"
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    print(response.text)

def run_my():

    url = "http://192.168.50.131:8091/encode"

    payload = {"id": 111,"texts": ["我想查花费"],"is_tokenized": False}
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "03825798-b9fb-7776-8f55-8fd28d4a0806"
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    print(response.text)


def call_gevent(count):
    """调用gevent 模拟高并发"""
    begin_time = time.time()
    run_gevent_list = []
    for i in range(count):
        print('--------------%d--Test-------------' % i)
        run_gevent_list.append(gevent.spawn(run_my()))
    gevent.joinall(run_gevent_list)
    end = time.time()
    print('单次测试时间（平均）s:', (end - begin_time) / count)
    print('累计测试时间 s:', end - begin_time)


if __name__ == '__main__':
    # 10万并发请求
    test_count = 100000
    call_gevent(count=test_count)
