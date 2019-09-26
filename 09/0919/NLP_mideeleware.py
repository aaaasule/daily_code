# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: NLP_mideeleware.py
@time: 2019/9/19 14:18
"""
import json
import pymysql
from flask import Flask, request
import redis
import requests
import time

"""
每一个用户的每轮会话都应该记录下来
"""

app = Flask(__name__)

# 映射租户id和容器ipID的字典(一个list)
map_dict = {
    1: ["127.0.0.1", "ip_2", "ip_3", "ip_4"],
    2: ["127.0.0.1", "ip_2", "ip_3", "ip_4"],
    3: ["127.0.0.1", "ip_2", "ip_3", "ip_4"],
    4: ["127.0.0.1", "ip_2", "ip_3", "ip_4"]
}

# 规定端口号
port = [8000, 8080, 8001]

# 使用redis缓存来记录访客id和容器IP的对应关系
conn = redis.Redis(host="127.0.0.1", port=6379, password="123456")

"""
# 连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root',db='test',charset='utf8')

# 设置游标
consor = conn.cursor()
sql = ''
consor.execute(sql)

# 先关闭游标
consor.close()

# 再关闭连接
conn.close()
"""


# 暴露给用户说那边的接口,用于接收参数
@app.route('/api/nlp_tenement_middleware/', methods=["POST"])
def nlp_interface():
    """
    lessee_id 租户ID   租户ID--一个租户ID对应的是一类服务器，比如租户是移动的，那么这个租户Id对应的有一个列表ip,列表中每一个ip对应的服务器都是为移动做的模型
    visitor_id 访客ID  每一个访客第一次进来说第一句话的时候都会分配一个id(唯一的)，第二句话就根据这个id对应的ip来继续对话；第二次进来又重新分配了一个id
    question 问题  用户说
    record_id 回话ID  用户说的第一句话请求时recordID是空的，我这边返回了一个id,第二句话来请求我，recordID就是我给的
    apiKey 校验用户身份 用来校验用户身份的，现在是写死的，以后会根据其他方法来进行校验 每隔两小时验证一次
    """
    params = request.json
    lesseeId = params["lesseeId"]
    visitorId = params["visitorId"] # vsitorId会有重复的可能吗？
    question = params["question"]
    recordId = params["recordId"]
    apiKey = params["apiKey"]

    # 获取apiKey
    def getApiKey():
        apiKey = "e10adc3949ba59abbe56e057f20f883e"
        return apiKey

    # 校验apiKey 两小时一次
    def checkApiKey(apiKey):

        if apiKey == getApiKey():
            return True

    # 分配路由 依据规则
    def allocateRoute(lesseeId, visitorId, question, recordId):

        # 确认租户Id来在寻找对应的容器IP列表 如果有就查找
        if map_dict[lesseeId]:
            containIps = map_dict[lesseeId]
            """
            具体应该选择的容器是哪一个, 怎么定？
            """
            # 根据访客ID来指定容器
            conn.set(visitorId, containIps[0])

            if recordId == " ":
                recordId = params["visitorId"]
            else:
                pass


        else:
            pass

        url = "http://{}".format(containIps[0])
        data = {"visitorId": visitorId, "question": question}
        return url, data, recordId

    # 调用容器中的模型  并返回规定的参数给用户
    def postContainModel(url, data):
        print('data-->',data)
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            'postman-token': "dab24781-8945-79b8-de26-cd5c2de6bba3"
        }

        response = requests.request("POST", url, data=json.dumps(data), headers=headers)

        return response.text

    # 记录每一个用户的会话流程 ？使用MySQL来记录用户的会话  id 访问时间
    def recordSession():
        pass


    if checkApiKey(apiKey):
        url, data, recordId = allocateRoute(lesseeId, visitorId, question, recordId)
        postUrl = url + ':8000' + '/index/'

        postContainResponse = postContainModel(url=postUrl,data=data)

    return json.loads(postContainResponse)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8001, debug=True)
