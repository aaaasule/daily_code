# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 0016 9:47
# @Author  : Zhang
# @File    : 调整数据量.py

#得到数据中各个标签的数量   ['修改', '重置', '咨询', '预约', '办理', '查询', '具实', '开通', '确认', '取消']

label_ten = ['修改', '重置', '咨询', '预约', '办理', '查询', '具实', '开通', '确认', '取消']
label_fourth = ['预约宽带', '取消', '查询套餐余量', '确认1', '查询流量', '修改宽带', '重置', '修改',
                 '查询套餐外短彩信费', '取消流量', '具实重听', '咨询宽带', '查询套餐及固定费', '具实退出',
                '重置宽带', '具实帮助', '查询套餐外上网费', '办理', '查询语音通信费', '重置手机', '查询短信',
                '查询协议消费差额', '查询', '查询积分', '查询增值业务费', '开通', '查询账单', '咨询', '具实返回',
                '查询语音', '查询月初扣费', '查询余额', '查询本机业务', '查询他人付费', '查询充值缴费记录', '办理套餐',
                '办理手机充值', '具实转ivr', '修改手机', '具实转人工', '开通流量', '查询本机号码']
def get_label_num(file_dir,list):
    with open(file_dir,"r",encoding="utf-8") as f:
        data = f.readlines()
        print(len(data))
        labels = list

        for n in range(len(list)):
            count = 0
            for i in data:
                if i.split()[0] == labels[n]:
                    count += 1
                else:
                    pass
            print(labels[n],"===》",count)
# r'D:/PycharmProjects/work_space/code/08/0814/fours_test.tsv'

# get_label_num(r'D:/PycharmProjects/work_space/code/08/0815/fours_test.tsv')
get_label_num(r'D:/PycharmProjects/work_space/code/08/0815/ten_train.tsv',label_ten)
