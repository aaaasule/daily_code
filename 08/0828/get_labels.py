file_dir = 'g:/PyCharmProjects/daily_code/09/0905/data/train.tsv'

with open(file_dir,'r',encoding='utf-8') as fp:
    datas = fp.readlines()
    print(datas)
    list_labels = []
    for i in datas:
        # print(i.split('\t'))
        list_labels.append(i.split('\t')[0])

print(set(list_labels))

labels = ['具实', '预约', '确认', '修改', '开通', '办理', '查询', '咨询', '取消', '重置']