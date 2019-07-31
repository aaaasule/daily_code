with open("origan.txt",'r',encoding='utf-8') as f:
    data = f.readlines()
    print(data)
    print(type(data))
    data_list = list()
    for i in data:
        data_list.append(i)
    print(data_list)
    with open('data.txt','w',encoding='utf-8') as f1:
        for j in data_list:
            print(j)
            f1.write(j[0:-1] + " nt\n")
