# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: 请求接口.py
@time: 2019/9/20 14:20
"""

import requests
import json
url = "http://192.168.50.131:8081/encode"

payload = {
    "id": 11,
    "texts": ["喂你好我想问一下我的业务套餐是多少钱的"],
    "is_tokenized": False
}
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "8463fb3a-b0dd-bb43-8170-18ca7ccd6b85"
    }

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

print(response.text)