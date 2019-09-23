# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: test_r_interface.py
@time: 2019/9/20 14:04
"""
from flask import Flask
from flask import request
from bert_base.client import BertClient

import json

app = Flask(__name__)

@app.route('/api/server/', methods=["POST"])
def selecetModel():
    # 获取请求参数
    params = request.json
    print(params)
    id = params["id"]
    list_text = params["text"]

    def bertModel(id,list_text):

        with BertClient(ip='192.168.50.131', port=5575, port_out=5576, show_server_config=False, check_version=False,
                        check_length=False, timeout=10000, mode='CLASS') as bc:
            rst = bc.encode(list_text)
            rst[0]["id"] = id
        return rst[0]

    resp_bert = bertModel(id=id, list_text=list_text)

    return resp_bert





app.run(host="127.0.0.1", port=8080, debug=True)
