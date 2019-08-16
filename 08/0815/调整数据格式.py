# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 0015 9:00
# @Author  : Zhang
# @File    : 调整数据格式.py

def get_data(file_data,file_goal,):
    with open(file_data,'r',encoding='utf-8') as f:# D:/PycharmProjects/work_space/code/08/0814/ten_test.tsv
        data = f.readlines()
        label_alls = list()
        with open(file_goal, 'w', encoding='utf-8') as f1: # D:/PycharmProjects/work_space/code/08/0815/ten_test.tsv
            for i in data:
                # 获取每一个元素的标签  ['修改', '重置', '咨询', '预约', '办理', '查询', '具实', '开通', '确认', '取消']
                label_alls.append(i.split()[0])
                labels = list(set(label_alls))
            for n in range(len(labels)):
                print(n)
                for j in data:
                    if j.split()[0] == labels[n]:
                        f1.write(j)

get_data(r'D:/PycharmProjects/work_space/code/08/0814/fours_test.tsv',r'D:/PycharmProjects/work_space/code/08/0815/fours_test.tsv')

