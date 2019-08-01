# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 0001 17:58
# @Author  : Zhang
# @File    : 换个思路来标注数据.py
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 0001 14:33
# @Author  : Zhang
# @File    : 新的标注数据.py
# -*- coding: utf-8 -*-
# @Time    : 2019/7/31 0031 14:39
# @Author  : Zhang
# @File    : 标注数据.py

"""写一个标注文本的软件包，单条语句输入，输出一个标注好的文本（依据不同类型来输出）"""

import xlrd
import random


def extra_excel_data(fileName, sheetName, cols):
    data = xlrd.open_workbook(fileName)

    table = data.sheet_by_name(sheet_name=sheetName)

    data_value = table.col_values(cols, start_rowx=2, end_rowx=None, )

    return data_value


def extra_txt_data(fileName):
    names = []
    with open(fileName, 'r', encoding='utf8') as f:
        txt_value = f.readlines()
        for name in txt_value:
            name = name[:-1]
            names.append(name)
        return names

def tag_name(name):
    name_list = []
    len_name = len(name)
    for i in range(0,len_name):
        if i == 0:
            taged_name = name[i] + '\tB-PER'
            name_list.append(taged_name)
        else:
            taged_name = name[i] + '\tI-PER'
            name_list.append(taged_name)
    return name_list

def tag_location(location):
    loca_list = []
    len_location = len(location)
    for i in range(0, len_location):
        if i == 0:
            taged_location = location[i] + '\tB-LOC'
            loca_list.append(taged_location)
        else:
            taged_location = location[i] + '\tI-LOC'
            loca_list.append(taged_location)
    return loca_list

def get_index(list):
    list_k = []
    for k,v in enumerate(list):
        if v == '{':
            print('k==>',k)
            list_k.append(k)
    return list_k

langu_tem_names = ['你好！我叫{}', '你好！我的名字是{}', '很高兴认识你，我叫{}', '很高兴认识你，我的名字是{}',
                   '您好！我叫{}', '您好！我的名字是{}', '请问您是{}?', '我是{}', '{}，您好', '我是{}',
                   '您好！我是{}', '你好，我是{}', '我叫{}', '我的名字是{}', '我的名字叫{}', '请问您是{}吗',
                   '您的姓名是{}吗', '您是{}吗', '{}您好', '{}女士您好', '{}先生您好', '您好，请问是{}女士吗',
                   '您好，请问是{}先生吗', '您好，请问是{}吗']

langu_tem_locations = [
    '是{}', '在{}', '住在{}', '就在{}', '在那个{}',
    '我在{}', '我家在{}', '我住在{}', '我就在{}', '我就住在{}',
    '我家住在{}', '我家就在{}', '我公司在{}', '我公司就在{}', '我的公司在{}', '我的公司就在{}',
    '地址是{}', '地址在{}', '家庭地址是{}', '公司地址是{}', '我的地址是{}', '我的地址就是{}', '我的地址在{}',
    '我的地址就在{}', '我的地址是在{}', '我家地址是{}', '我家地址在{}', '我家地址是在{}', '我家的地址是{}', '我家的地址在{}',
    '我家的地址是在{}', '请送到{}，谢谢', '送到{}', '邮到{}', '帮我邮寄到{}', '帮我寄到{}', '你来{}，我家就在这', '在{}那边',
    '你记一下我的地址，{}', '你记一下，{}', '{}，记下来了吗', '啊，就在那个{}', '请问您的地址是不是{}', '请问您的地址是不是{}',
    '请问您的地址是不是{}', '学校在{}', '学校地址是{}', '我要去{}', '帮我查一下{}附近的医院', '我在{}附近', '请来{}接我', '嗯，我家在{}',
    '对！我就住在{}', '好的，具体地址是{}', '你到{}这儿来就可以找到我了', '你是说你家在{}，对吗？', '我们公司在{}?', '我要去{}旁边的医院看病',
    '我住在{}', '{}', '地址是{}吗?', '您是住在{}吗?'
]

langu_tem_loca_names = ['你好！我是{}，我家在{}', '那个,{}的家是{}', '你好！我的名字是{}，我想叫一辆去{}的车',
                        '请问您是{}用户，住在{}吗？', '您好！您是{}用户，家在{}吗？', '{}您好！您的现住址还是{}吗？',
                        '你好！我叫{}我在{}', '你好！我叫{}我就住在{}', '你好！我叫{}我家就在{}', '你好！我叫{}我公司就在{}',
                        '你好！我叫{}我家地址是在{}', '你好！我叫{}你来{}，我家就在这', '你好！我叫{}你记一下我的地址，{}',
                        '你好！我叫{}啊，就在那个{}', '你好！我的名字是{}住在{}', '你好！我的名字是{}我的公司在{}',
                        '你好！我的名字是{}请送到{}，谢谢', '你好！我的名字是{}帮我邮寄到{}', '你好！我的名字是{}你记一下我的地址，{}',
                        '很高兴认识你，我叫{}家庭地址是{}', '很高兴认识你，我叫{}公司地址是{}', '您好，请问是{}住在{}吗?',
                        '您好，请问是{}女士吗帮我查一下{}附近的医院', '您好，请问是{}女士吗我家地址是{}'
                        ]

if __name__ == '__main__':

    huiSuo_locations = extra_excel_data('会所 11.xls', '数据列表1', 1)

    bot_locations = extra_excel_data('机器人，广告屏等11.xls', '数据列表1', 1)

    personNames = extra_txt_data('常用汉语人名大全.txt')  # 24042

    # 人名 --> B-Per  I-Per    地址名 -->  B-Loc I-Loc

    with open('tag_data_2.txt', 'w', encoding='utf8') as f:

        # 只添名字
        for _ in range(4500):
            name = random.choice(personNames[0:12021])
            tem_n = random.choice(langu_tem_names)
            list_name = []
            for n in tem_n:
                list_name.append(n)
            start_name_index = tem_n.index('{')
            list_name.insert(start_name_index,tag_name(name))
            list_name.remove('{')
            list_name.remove('}')
            # print(list_1)
            for i in list_name:
                if len(i) == 1:
                    f.write(i+'\tO\n')
                else:
                    for j in list(i):
                        f.write(j+'\n')
            f.write('\n')


        # 只添地址
        locations = list(set(huiSuo_locations + bot_locations))
        for _ in range(4500):
            location = random.choice(locations[0:2367])
            tem_l = random.choice(langu_tem_locations)
            list_location = []
            for l in tem_l:
                list_location.append(l)
            start_loca_index = tem_l.index('{')

            list_location.insert(start_loca_index, tag_location(location))
            list_location.remove('{')
            list_location.remove('}')

            for i in list_location:
                if len(i) == 1:
                    f.write(i + '\tO\n')
                else:
                    for j in list(i):
                        f.write(j + '\n')
            f.write('\n')


        # 添加地址和名字
        for _ in range(10000):
            tem_n_l = random.choice(langu_tem_loca_names)
            name = random.choice(personNames[12021:])
            location = random.choice(locations[2367:])
            list_location_name = []
            for n_l in tem_n_l:
                list_location_name.append(n_l)
            k_1 = get_index(tem_n_l)[0]
            k_2 = get_index(tem_n_l)[1]

            list_location_name.insert(k_1,tag_name(name))
            list_location_name.insert(k_2+1,tag_location(location))
            list_location_name.remove('{')
            list_location_name.remove('}')
            list_location_name.remove('{')
            list_location_name.remove('}')

            for i in list_location_name:
                if len(i) == 1:
                    f.write(i + '\tO\n')
                else:
                    for j in list(i):
                        f.write(j + '\n')
            f.write('\n')




