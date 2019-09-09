# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: 并发测试.py
@time: 2019/9/6 11:14
"""
import json

import requests
from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()

from flask import Flask
import time

app = Flask(__name__)

@app.route()
def testpost():
    url = "http://192.168.230.129:5000/"

    payload = {
        "list": ["我在胜古中路1号"]
    }
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "363fcb86-c76a-57f5-dc39-d1d9bdd05d9d"
    }

    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

    print(response.text)

