# -*- coding:utf-8 -*-
# 年的集合
nums_years = [str(num) + '年' for num in range(1995,2020)]
# 月的集合
list_mouths = ['一','二','三','四','五','六','七','八','九','十','十一','十二']
nums_mouths = [str(num) + '月' for num in range(1,13)]
# 天的集合
nums_day_31 = [str(n) + '号' for n in range(1,32)]
nums_day_30 = [str(n) + '号' for n in range(1,31)]
num_day_28 = [str(n) + '号' for n in range(1,29)]
num_day_29 = [str(n) + '号' for n in range(1,30)]
# 小时的集合
nums_hours = [str(n) + '点' for n in range(1,25)]

# 分的集合
nums_mins = [str(n) + '分' for n in range(1,61)]
# 秒的集合
nums_secs = [str(n) + '秒' for n in range(1,61)]

# 拼接年和月
year_mouths = list()
for year in nums_years:
    for mouth in nums_mouths:
        year_mouths.append(year + mouth)
# 拼接年 月 日
year_mouth_days = list()
for year in nums_years:
    for mouth in nums_mouths:
        if int(year[:-1])%4:# 非闰年
                if int(mouth[:-1]) in [1,3,5,7,8,10,12]:
                    for day in nums_day_31:
                        year_mouth_days.append(year + mouth + day)
                elif int(mouth[:-1]) == 2:
                    for day in num_day_28:
                        year_mouth_days.append(year + mouth + day)
                else:
                    for day in nums_day_30:
                        year_mouth_days.append(year + mouth + day)
        else: # 闰年
                if int(mouth[:-1]) in [1,3,5,7,8,10,12]:
                    for day in nums_day_31:
                        year_mouth_days.append(year + mouth + day)
                elif int(mouth[:-1]) == 2:
                    for day in num_day_29:
                        year_mouth_days.append(year + mouth + day)
                else:
                    for day in nums_day_30:
                        year_mouth_days.append(year + mouth + day)

# 拼接 月 日
mouth_days = list()
for mouth in nums_mouths:

    if int(mouth[:-1]) in [1, 3, 5, 7, 8, 10, 12]:
        for day in nums_day_31:
            mouth_days.append(mouth + day)
    elif int(mouth[:-1]) == 2:
        for day in num_day_29:
            mouth_days.append(mouth + day)
    else:
        for day in nums_day_30:
            mouth_days.append(mouth + day)

# 拼接 日 时
day_hours = list()
for day in nums_day_31:
    for hour in nums_hours:
        day_hours.append(day + hour)

# 拼接 日 时 分
day_hour_mins=list()
for day in nums_day_31:
    for hour in nums_hours:
        for min in nums_mins:
            day_hour_mins.append(day + hour + min)

# 拼接 时 分 秒
hour_min_secs = list()
for hour in nums_hours:
    for min in nums_mins:
        for sec in nums_secs:
            hour_min_secs.append(hour + min + sec)
for hour in nums_hours:
    for min in nums_mins:
        for sec in nums_secs:
            hour_min_secs.append(hour[:-1] + ':' + min[:-1] + ':' + sec[:-1])

# 拼接 分 秒
min_secs = list()
for min in nums_mins:
    for sec in nums_secs:
        min_secs.append(min + sec)
print(min_secs)



time_words = list()
time_words.extend(nums_years)
time_words.extend(year_mouths)
time_words.extend(year_mouth_days)
time_words.extend(mouth_days)
time_words.extend(day_hours)
time_words.extend(day_hour_mins)
time_words.extend(hour_min_secs)
time_words.extend(min_secs)
time_words.extend(nums_hours)
with open('times.txt','w',encoding='utf8') as f:
    for word in time_words:
        f.write(word + ' t\n')