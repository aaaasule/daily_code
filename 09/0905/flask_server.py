# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: flask_server.py
@time: 2019/9/5 11:03
"""
from flask import Flask

app = Flask('__main__')

@app.route('/')
def test():
    return "hello flask!"


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)