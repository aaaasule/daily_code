# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: Test_middleware.py
@time: 2019/9/27 9:33
"""
from flask import Flask
from flask import request
import redis

# redis 用于记录访客id 和 容器Ip 的对应关系
conn = redis.Redis(host='127.0.0.1', port=6379, password='123456' )

# 映射租户id和容器ipID的字典(一个list)  映射关系通过访问一个接口来调用
mapDict = {
    1: "127.0.0.1",
    2: "127.0.0.1",
    3: "127.0.0.1",
    4: "127.0.0.1"
}


app = Flask(__name__)

class TenementModdleware(object):

    def __init__(self, tenementId, visitorId, question, recordId, apiKey, getApiKeyApi, getMapApi):
        self.tenementId = tenementId
        self.visitorId = visitorId
        self.question = question
        self.recordId = recordId
        self.apiKey = apiKey
        self.getApiKeyApi = getApiKeyApi
        self.getMapApi = getMapApi

    def getApiKay(self):
        """请求一个接口来获取apiKey"""
        apiKey = "e10adc3949ba59abbe56e057f20f883e"
        return apiKey

    def checkApiKey(self):
        """校验apiKey 两小时一次"""
        if self.apiKey == self.getApiKey(self):
            return True

    def getMap(self):
        """获取租户和容器的对应关系"""
        pass

    def setRecordId(self):
        """设置访客id"""
        pass

    def allocateRoute(self):
        """分配路由"""
        pass

    def postContainModel(self):
        """调用容器中的NLP, 返回参数"""
        # 确认租户Id来在寻找对应的容器IP列表 如果有就查找
        if mapDict[self.tenementId]:
            containIps = mapDict[self.tenementId]
            """
            同一个租户对应使用一个容器，只有当前容器达到了预设的并发量时，才会启动另一台容器
            """
            # 访客第一次请求的recordId值是空的
            if self.recordId == " ":  # 第一次请求是Flase
                # 根据访客ID来指定容器 设置过期时间（ex= 单位是秒，px= 单位是毫秒）
                conn.set(self.visitorId, containIps[0], ex=180)
                recordId_1 = params["visitorId"]
                print("recordId_1------>", recordId_1)
            else:

                recordId_1 = recordId

            data = {"visitorId": visitorId, "question": question, "recordId": recordId_1}
            url = "http://{}".format(containIps[0])
        return url, data, recordId_1

    def recordSession(self):
        """记录会话流程"""
        pass



@app.route('/api/tenement_middleware/', methods=["POST"])
def tenement_interface():
    if request.method == "POST":

        params = request.json

        tenementId = params["tenementId"]
        visitorId = params["visitorId"]
        question = params["question"]
        recordId = params["recordId"]
        apiKey = params["apiKey"]



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)