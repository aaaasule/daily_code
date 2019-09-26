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

@app.route('/index/', methods=["POST"])
def index():
    params = request.json
    id = params["visitorId"]
    text = params["question"]
    recordID = params["recordId"]
    response = {"id": id, "text": text, "recordId": recordID}
    return response


app.run("0.0.0.0",port=8000)