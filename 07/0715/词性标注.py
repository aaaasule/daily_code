# -*- coding:utf-8 -*-
import os
import jieba
file_name = "times.txt"
jieba.load_userdict(file_name)
import jieba.posseg as pseg
words = pseg.cut("我2019年7月16日早上8点去学校，晚上八点回来")
for word, flag in words:
    print('%s, %s' % (word, flag))




# get_module_res = lambda *res: open(os.path.normpath(os.path.join(os.getcwd(), os.path.dirname(__file__), *res)), 'rb')
# resp = get_module_res("posseg","prob_start.p")
# print(resp)