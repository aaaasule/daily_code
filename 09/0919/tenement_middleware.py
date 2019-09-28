# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: tenement_middleware.py
@time: 2019/9/19 14:18
"""
import json
import pymysql
from flask import Flask, request
from threading import Timer
import redis
import requests
import time
import uuid

"""
每一个用户的每轮会话都应该记录下来
"""

app = Flask(__name__)

# 映射租户id和容器ipID的字典(一个list)  映射关系通过访问一个接口来调用
mapDict = {
    1: "127.0.0.1",
    2: "127.0.0.2",
    3: "127.0.0.3",
    4: "127.0.0.4",
}


# 使用redis缓存来记录访客id和容器IP的对应关系
conn = redis.Redis(host="127.0.0.1", port=6379, password="123456")


# 暴露给用户说那边的接口,用于接收参数
@app.route('/api/tenement_middleware/', methods=["POST"])
def tenement_interface():
    params = request.json
    tenementId = params["tenementId"]
    visitorId = params["visitorId"]
    question = params["question"]
    recordId = params["recordId"]
    apiKey = params["apiKey"]

    # 获取apiKey 可以使用uuid
    def getApiKey():
        apiKey = "e10adc3949ba59abbe56e057f20f883e"
        return apiKey

    # 校验apiKey 两小时一次
    def checkApiKey(apiKey):

        task = Timer(interval=2 * 3600, function=checkApiKey, args=(apiKey,))
        task.start()

        if apiKey == getApiKey():
            return True
        else:
            return False

    # 获取租户和容器的对应关系
    def getRelation():
        pass

    # 设置访客ID
    def setRecordId(id):
        pass

    # 分配路由 依据规则
    def allocateRoute(tenementId, visitorId, question, recordId):

        # 确认租户Id来在寻找对应的容器IP列表 如果有就查找
        if mapDict[tenementId]:
            containIp = mapDict[tenementId]

            # 访客第一次请求的recordId值是空的
            if recordId == " ":  # 第一次请求是空
                # 根据访客ID来指定容器 设置过期时间（ex= 单位是秒，px= 单位是毫秒）
                conn.set(visitorId, containIp, ex=180)
                recordId_m = params["visitorId"]
            else:
                conn.set(visitorId, containIp, ex=180)
                recordId_m = recordId

            data = {"visitorId": visitorId, "question": question, "recordId": recordId_m}
            url = "http://{}".format(containIp)
        return url, data

    # 调用容器中的模型  并返回规定的参数给用户
    def postContainModel(url, data):
        print('data-->', data)
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            'postman-token': "f013961e-d7d7-843f-388a-ad94e850383e"
        }
        response = requests.request("POST", url, data=json.dumps(data), headers=headers)
        print(response.text)
        return response.text

    # 记录每一个用户的会话流程 ？使用MySQL来记录用户的会话  id 访问时间
    def recordSession():
        pass


    if checkApiKey(apiKey):

        url, data = allocateRoute(tenementId, visitorId, question, recordId)

        return {'url': url, 'data': data}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8001, debug=True)
