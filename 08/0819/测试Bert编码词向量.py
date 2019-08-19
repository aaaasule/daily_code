# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 0019 10:34
# @Author  : Zhang
# @File    : 测试Bert编码词向量.py

from bert_serving.client import BertClient

bc = BertClient()

ad = bc.encode(['查一下话费有多少','我需要个三十元加油包','帮我查一下我的话费还有多少钱'])

print(ad)