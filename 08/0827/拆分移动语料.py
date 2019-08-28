
import random

data_dir = "e:/PyCharmProjects/daily_code/08/0815/ten_train.tsv"

with open(data_dir,'r',encoding='utf-8') as fp:

    datas = fp.readlines()


    random.shuffle(datas) # 打乱有序列表 1066 * 10，比例  6 : 2 : 2

print(datas)

# 把datas分成data_train、data_test、data_dev三个文件元素比例 6 2 2
data_train = datas[:1066*6]

data_test = datas[1066*6:1066*(6 + 2)]

data_dev = datas[1066*(6 + 2):-1]

#将列表中元素写入tsv文件中

def write_tsv(list,file_name):
    with open(file_name,'w',encoding='utf-8') as fp:

        for text in list:
            fp.write(text)
    fp.close()


file_dir = 'e:/PyCharmProjects/daily_code/08/0828/'

write_tsv(data_train,file_dir + 'data_train.tsv')
write_tsv(data_test,file_dir + 'data_test.tsv')
write_tsv(data_dev,file_dir + 'data_dev.tsv')
