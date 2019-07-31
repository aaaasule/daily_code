# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 0026 12:50
# @Author  : Zhang
# @Site    : 
# @File    : 测试文件.py
# @Software: PyCharm



langu_tem_names= ['你好！我叫{}','你好！我的名字是{}']

langu_tem_locations = [
            '是{}','在{}','住在{}','就在{}','在那个{}',
                ]
langu_tem_loca_names = ['你好！我是{}，我家在{}','那个,{}的家是{}','你好！我的名字是{}，我想叫一辆去{}的车'
                        ]

names = [
'艾朝瑛','艾福聪','艾昊'
]

locations = [
'location1','location2','location3'
]

with open('data_test.txt','w',encoding='utf8') as f:
    for tem_langu in langu_tem_loca_names:
        for name in names:
            tem_name = tem_langu.format(name,{})
            for location in locations:
                tem_name_loca = tem_name.format(location)
                f.write(tem_name_loca + '\n')


