# -*- coding:utf-8 -*-
# 关键词抽取算法主要有两类

# 有监督学习算法：将关键词抽取过程视为二分类问题，先抽取出候选词，然后对于每个候选词划定标签，要么是关键词，要么不是关键词，然后训练关键词抽取分类器。当新来一篇文档时，抽取出所有的候选词，然后利用训练好的关键词抽取分类器，对各个候选词进行分类，最终将标签为关键词的候选词作为关键词；

# 无监督学习：先抽取出候选词，然后对各个候选词进行打分，然后输出topK个分值最高的候选词作为关键词。根据打分的策略不同，有不同的算法，例如TF-IDF，TextRank等算法；


# 基于TF-IDF算法进行关键词抽取
from jieba import analyse
# 引入TF-IDF关键词抽取接口
tfidf = analyse.extract_tags

# 原始文本
# text = "星期天上午，风和日丽，我们一家人开车前往二郎山游玩。 到了地方，我们一步一步地爬上了山顶，累得气喘吁吁。站在山上，我远远看到，两座山峰之间有一座玻璃桥。听爸爸说这就是玻璃栈道。我们走到栈桥跟前，只见玻璃栈道桥上的人似乎对这座桥充满了恐惧"
text = "我今天八点去学校"
# 基于TF-IDF算法进行关键词抽取
keywords = tfidf(text)
# print("keywords====>",keywords)
# 输出抽取出的关键词
for keyword in keywords:
    pass
    # print(keyword + "/",)



# 基于TextRank算法进行关键词抽取
textrank = analyse.textrank

keywords_textrank = textrank(text,allowPOS=('t','ts'))

# 输出抽取出的关键词
for keyword_textrank in keywords_textrank:
    print(keyword_textrank + "/",)
