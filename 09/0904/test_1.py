# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: test_1.py
@time: 2019/9/4 9:46
"""
import re

text = '{"sentence": "查话费叠加呢", "intents": [{"action": {"value": "查询"}, "target": {"value": "余额"}}], "slots": []}'

d = re.findall('{"sentence": "(.{0,})", "intents":',text)
d1 = re.findall('{"value": "(.{0,})"}, "target":',text)
print(d[0])
print(type(d))
print(d1)





# with open(r"G:\下载\people-2014\test\0123\c1001-24200319.txt",'r',encoding='utf-8') as fp:
#     datas = fp.readlines()
#
#
#     for text in datas:
#         print('text--->',text)
#         rf = re.findall("([a-z])(\d?)",text)
#         # 将所有匹配到的pattern 放在一个列表中
#         rfs = list()
#         for i in rf:
#             r = str()
#             for j in list(i):
#                 r += j
#             rfs.append(r)
#         for f in rfs:
#             text = text.replace(f,'')
#         print('text--->',text)
#
#
#         data = ''
#         for t in text:
#             if t not in ['[',']','/']:
#                 data += t
#         print(data.replace(' ',''))



            # d = re.findall("(/)([a-z]{1,4})([0-9])",text)
            # print(d)
            # d[0] =
            # print(type(d[0]))

    #     for i in text:
    #         i.replace("(/)([a-z]{1,4})([0-9]{0,1})",'')
    #         data += i
    # print(data)

    # st = "/n1那是肯定拿到/n2"
    # r = re.findall("(/)([a-z]{1,4})([0-9])",st)
    # st = st.replace('/n1','')
    # print(st)
    # print(r)