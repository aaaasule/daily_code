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
import random
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
@app.route('/api/nlp_tenement/', methods=["POST"])
def nlp_interface():
    params = request.json
    id = params["id"]
    text = params["text"]
    # print(params)
    # 通过map_dict 来将用户指向对应的容器 IP
    # contain_ip = map_dict[id]
    contain_ip = "192.168.50.131"
    """
     同一个用户ID对应的几个容器如何选择,只选择一个容器
    """
    #调用容器中的模型
    def bertModel(id, contain_ip, list_text):
        with BertClient(ip=contain_ip, port=5575, port_out=5576, show_server_config=False, check_version=False,
                        check_length=False, timeout=10000, mode='CLASS') as bc:
            rst = bc.encode(list_text)
            rst[0]["id"] = id
        return rst[0]

    # 容器返回的结果
    resp_bert = bertModel(id=id, contain_ip=contain_ip, list_text=text)

    """将返回的结果给到对应ID的用户"""
    def retutn_goal():
        print(resp_bert)

    return True

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8001, debug=True)
