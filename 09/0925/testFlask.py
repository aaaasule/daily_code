# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: testFlask.py
@time: 2019/9/25 17:20
"""

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/getAnswerByRobot/', methods=["POST"])
def index():
    params = request.json

    id = params["visitorId"]
    text = params["question"]
    recordId = params["recordId"]

    response = {"id": id, "text": text, "recordId": recordId}

    return response


app.run(host="0.0.0.0",port=8080)