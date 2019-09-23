# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: NLP_mideeleware.py
@time: 2019/9/19 14:18
"""
from flask import Flask, request
from bert_base.client import BertClient

"""
1、从用户说那边接收参数（我这边可以写一个接口来接受参数）
2、将用户说的参数传给用户ID对应的容器ID
3、容器返回的内容在传回给用户
"""

app = Flask(__name__)

# 映射用户id和容器ipID的字典(一个list)
map_dict = {}


# 暴露给用户说那边的接口,用于接收参数
# 需要的参数：1,用户ID 2,用户说text 3,
@app.route('/get_json/', methods=["POST"]) # http://127.0.0.1:8001/get_json/?id=1&text=["我想查话费"]/
def get_json():
    params = request.json
    id = params["id"]
    text = params["text"]
    print(params)

    def bertModel(id,list_text):

        with BertClient(ip='192.168.50.131', port=5575, port_out=5576, show_server_config=False, check_version=False,
                        check_length=False, timeout=10000, mode='CLASS') as bc:
            rst = bc.encode(list_text)
            rst[0]["id"] = id
        return rst[0]

    resp_bert = bertModel(id=id,list_text=text)

    return resp_bert


# 将用户说那边的数据参数传到对应的容器里   依据一定的逻辑来指定对应的容器
# @app.route('/send_json')
# def send_json():
#     contain_url = ""


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8001, debug=True)
