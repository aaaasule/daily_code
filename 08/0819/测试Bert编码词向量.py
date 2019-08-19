# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 0019 10:34
# @Author  : Zhang
# @File    : 测试Bert编码词向量.py

from bert_serving.client import BertClient

# bc = BertClient(ip="192.168.50.55")
bc = BertClient(ip="47.93.9.85")
bc.encode([])