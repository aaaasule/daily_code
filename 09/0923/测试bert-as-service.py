# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: 测试bert-as-service.py
@time: 2019/9/23 10:16
"""
from flask import Flask
from flask import request
from bert_base.client import BertClient
import time


app = Flask(__name__)

@app.route('/api/server/',methods=["POST"])
def class_pred():
    # 获取请求参数
    params = request.json
    print(params)
    id = params["id"]
    list_text = params["text"]
    #文本拆分成句子
    #list_text = cut_sent(text)
    print("total setance: %d" % (len(list_text)) )
    with BertClient(ip='192.168.50.131', port=5575, port_out=5576, show_server_config=False, check_version=False, check_length=False,timeout=10000 ,  mode='CLASS') as bc:
        start_t = time.perf_counter()
        rst = bc.encode(list_text)

        rst[0]["id"] = id
        print('result:', rst)
        print('time used:{}'.format(time.perf_counter() - start_t))
    #返回结构为：
    # rst: [{'pred_label': ['0', '1', '0'], 'score': [0.9983683228492737, 0.9988993406295776, 0.9997349381446838]}]
    #抽取出标注结果
    # pred_label = rst[0]["pred_label"]
    # result_txt = [ [pred_label[i],list_text[i] ] for i in range(len(pred_label))]
    # print(result_txt)
    # return result_txt[0]
    return rst[0]

app.run()

