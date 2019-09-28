# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: 定时校验.py
@time: 2019/9/28 11:11
"""
from flask import Flask
from threading import Timer
import time

app = Flask(__name__)
@app.route('/index/',methods=["POST"])
def index():
    return "hello!"

def taskName():
    print('zhang,14', time.ctime())
    t = Timer(interval=3, function=taskName, args=None, kwargs=None)
    t.start()

if __name__ == '__main__':

    taskName()

    app.run(debug=True)

