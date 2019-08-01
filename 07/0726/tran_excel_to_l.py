# -*- coding:utf-8 -*-
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

    huiSuo_locations = extra_excel_data('会所 11.xls','数据列表1',1)

    bot_locations = extra_excel_data('机器人，广告屏等11.xls','数据列表1',1)

    personNames = extra_txt_data('常用汉语人名大全.txt') # 24042



    with open('language_data_2.txt', 'w', encoding='utf8') as f:

        only_names = []
        for _ in range(4500):
            name = random.choice(personNames[0:12021])
            tem_n = random.choice(langu_tem_names)
            tem_name = tem_n.format(name)
            only_names.append(tem_name)
        only_names = list(set(only_names))

        all_names = ''
        for tem_na in only_names:
            all_names = all_names + ' ' + tem_na
        print(all_names)
        for i in all_names:

            f.write(i + ' O\n')





        # # 只添名字
        # only_names = []
        # for _ in range(4500):
        #     name = random.choice(personNames[0:12021])
        #     tem_n = random.choice(langu_tem_names)
        #     tem_name = tem_n.format(name)
        #     only_names.append(tem_name)
        # only_names = list(set(only_names))
        # for tem_na in only_names:
        #     f.write(tem_na + '\n')




        # # 只添地址
        # only_locations = []
        # locations = list(set(huiSuo_locations + bot_locations)) # 4735
        # for _ in range(4500):
        #     location = random.choice(locations[0:2367])
        #     tem_l = random.choice(langu_tem_locations)
        #     tem_location = tem_l.format(location)
        #     only_locations.append(tem_location)
        # only_locations = list(set(only_locations))
        # print(len(only_locations))
        # for tem_loc in only_locations:
        #     f.write(tem_loc + '\n')



        # # 添加地址和名字
        # loca_names = []
        # for _ in range(10000):
        #     tem_n_l = random.choice(langu_tem_loca_names)
        #     name = random.choice(personNames[12021:])
        #     location = random.choice(locations[2367:])
        #     tem_name_location = tem_n_l.format(name,location)
        #     loca_names.append(tem_name_location)
        # loca_names = list(set(loca_names))
        # print(len(loca_names))
        # for loca_name in loca_names:
        #     f.write(loca_name + '\n')