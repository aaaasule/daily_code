# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 0029 17:58
# @Author  : Zhang
# @File    : transfer_data.py

# -*- coding:utf-8 -*-
import xlrd


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

langu_tem_names= ['你好！我叫{}','你好！我的名字是{}','很高兴认识你，我叫{}','很高兴认识你，我的名字是{}',
                       '您好！我叫{}','您好！我的名字是{}','请问您是{}?','我是{}','{}，您好','我是{}',
                       '您好！我是{}','你好，我是{}','我叫{}','我的名字是{}','我的名字叫{}','请问您是{}吗',
                       '您的姓名是{}吗','您是{}吗','{}您好','{}女士您好','{}先生您好','您好，请问是{}女士吗',
                       '您好，请问是{}先生吗','您好，请问是{}吗']
langu_tem_locations = [
            '是{}','在{}','住在{}','就在{}','在那个{}',
            '我在{}','我家在{}','我住在{}','我就在{}','我就住在{}',
            '我家住在{}','我家就在{}','我公司在{}','我公司就在{}','我的公司在{}','我的公司就在{}',
            '地址是{}','地址在{}','家庭地址是{}','公司地址是{}','我的地址是{}','我的地址就是{}','我的地址在{}',
            '我的地址就在{}','我的地址是在{}','我家地址是{}','我家地址在{}','我家地址是在{}','我家的地址是{}','我家的地址在{}',
            '我家的地址是在{}','请送到{}，谢谢','送到{}','邮到{}','帮我邮寄到{}','帮我寄到{}','你来{}，我家就在这','在{}那边',
            '你记一下我的地址，{}','你记一下，{}','{}，记下来了吗','啊，就在那个{}','请问您的地址是不是{}','请问您的地址是不是{}',
            '请问您的地址是不是{}','学校在{}','学校地址是{}','我要去{}','帮我查一下{}附近的医院','我在{}附近','请来{}接我','嗯，我家在{}',
            '对！我就住在{}','好的，具体地址是{}','你到{}这儿来就可以找到我了','你是说你家在{}，对吗？','我们公司在{}?','我要去{}旁边的医院看病',
            '我住在{}','{}','地址是{}吗?','您是住在{}吗?'
                ]

langu_tem_loca_names = ['你好！我是{}，我家在{}','那个,{}的家是{}','你好！我的名字是{}，我想叫一辆去{}的车',
                        '请问您是{}用户，住在{}吗？','您好！您是{}用户，家在{}吗？','{}您好！您的现住址还是{}吗？',
                        '你好！我叫{}我在{}', '你好！我叫{}我就住在{}', '你好！我叫{}我家就在{}', '你好！我叫{}我公司就在{}',
                        '你好！我叫{}我家地址是在{}', '你好！我叫{}你来{}，我家就在这', '你好！我叫{}你记一下我的地址，{}',
                        '你好！我叫{}啊，就在那个{}', '你好！我的名字是{}住在{}', '你好！我的名字是{}我的公司在{}',
                        '你好！我的名字是{}请送到{}，谢谢', '你好！我的名字是{}帮我邮寄到{}', '你好！我的名字是{}你记一下我的地址，{}',
                        '很高兴认识你，我叫{}家庭地址是{}', '很高兴认识你，我叫{}公司地址是{}', '您好，请问是{}住在{}吗?',
                        '您好，请问是{}女士吗帮我查一下{}附近的医院', '您好，请问是{}女士吗我家地址是{}'
                        ]




if __name__ == '__main__':

    huiSuo_names = extra_excel_data('会所 11.xls','数据列表1',0)

    huiSuo_locations = extra_excel_data('会所 11.xls','数据列表1',1)

    bot_names = extra_excel_data('机器人，广告屏等11.xls','数据列表1',0)

    bot_locations = extra_excel_data('机器人，广告屏等11.xls','数据列表1',1)

    personNames = extra_txt_data('常用汉语人名大全.txt')

    # # 只添名字
    only_names = []
    with open('data.txt', 'a', encoding='utf8') as f:
        for name in personNames:
            for tem_name in langu_tem_names:
                langu_name_goal = tem_name.format(name)
                f.write(langu_name_goal)


    # # 只添地址
    only_locations = []
    with open('data.txt', 'a', encoding='utf8') as f:
        locations = huiSuo_locations + bot_locations
        # print('locations==>',locations)
        for location in locations:
            for tem_location in langu_tem_locations:
                langu_loca_goal = tem_location.format(location)
                f.write(langu_loca_goal)


    # # 添加地址和名字
    loca_names = []
    with open('language_data.txt', 'a',encoding='utf8') as f:
        for loca_name in langu_tem_loca_names:
            for name in personNames:
                loca_name_1 = loca_name.format(name,{})
                for location in locations:
                    loca_name_2 = loca_name_1.format(location)
                    f.write(loca_name_2 + '\n')
                    print('loca_name_2==>{}'.format(loca_name_2))