# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 0014 15:08
# @Author  : Zhang
# @File    : read_npy.py

import numpy as np

filtered_data = open(r"C:\Users\Administrator\Desktop\no_cut_data\filtered_data.txt",encoding='utf-8').read()

text_test = np.load(r"C:\Users\Administrator\Desktop\no_cut_data\text_test.npy")

text_train = np.load(r"C:\Users\Administrator\Desktop\no_cut_data\text_train.npy")

label_test = np.load(r"C:\Users\Administrator\Desktop\no_cut_data\label_test.npy")

label_train = np.load(r"C:\Users\Administrator\Desktop\no_cut_data\label_train.npy")

label_complex_test = np.load(r"C:\Users\Administrator\Desktop\no_cut_data\label_complex_test.npy")

label_complex_train = np.load(r"C:\Users\Administrator\Desktop\no_cut_data\label_complex_test.npy")


# text文档
text_tests = list()
for i in text_test:
    text_tests.append(i)

text_trains = list()
for i in text_train:
    text_trains.append(i)

# test和train标签  10个类
label_tests = list()
for i in label_test:
    label_tests.append(i)

label_trains = list()
for i in label_train:
    label_trains.append(i)

# test和train标签  40个类
label_complex_tests = list()
for i in label_complex_test:
    label_complex_tests.append(i)

label_complex_trains = list()
for i in label_complex_train:
    label_complex_trains.append(i)

def ten_label(list1,list2,file_dir):
    with open(file_dir,'w',encoding='utf-8') as f:
        for i in range(len(list1)):

            f.write(list1[i] + '\t' + list2[i] + '\n')

# ten_label(label_trains,text_trains,'ten_train.tsv')
# ten_label(label_tests,text_tests,"ten_test.tsv")
# ten_label(label_complex_tests,text_tests,'fours_test.tsv')
# ten_label(label_complex_trains,text_trains,'fours_train.tsv')

print(len(set(label_complex_tests)))
print(set(label_complex_trains))


