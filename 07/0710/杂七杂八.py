# -*- coding:utf-8 -*-

print(2019 % 4)
if 2016 % 4:
    print(True)
else:
    print(False)



list_mouths = ['一','二','三','四','五','六','七','八','九','十','十一','十二','十三','十四','十五','十六','十七','十八','十九','二十','二十一','二十二','二十三','二十四']
nums_hours = [str(n) + '点' for n in list_mouths]
print(nums_hours)
with open('time.txt','w') as f:
    for n in nums_hours:
        f.write(n + ' t\n')