# -*- coding: utf-8 -*-
"""
@version: ??
@author: zhang
@Mail: 123aaaasule@gmail.com
@file: python内存分配的小秘密.py
@time: 2019/9/6 10:05
"""
# 转自：https://my.oschina.net/u/4051725/blog/3100186
import sys
# getsizeof() 用于获取一个对象的字节大小（bytes）;只计算直接占用的内存，而不计算对象内所引用对象的内存
a = [1,2]
b = [a,a] # 即[[1,2],[1,2]]
print(sys.getsizeof(a))
print(sys.getsizeof(b))
"""
80
80
"""
# 一个静态创建的列表，如果自包含两个元素，那它自身占用的内存就是80个字节，不过其元素对象所指向的对象是什么。



#  1、空对象不是空的

print(sys.getsizeof(""))
print(sys.getsizeof([]))
print(sys.getsizeof(()))
print(sys.getsizeof(set()))
print(sys.getsizeof(dict()))

print(sys.getsizeof(1))
print(sys.getsizeof(True))
"""
49
64
48
224
240


28
28
"""
# 2、内存扩充是不均匀的
# 空对象并不为空，一部分原因是 Python 解释器为它们预分配了一些初始空间
# 还有一部分内存用于创建容器的骨架、记录容器的信息

import sys
letters = "abcdefghijklmnopqrstuvwxyz"

a = []
for i in letters:
    a.append(i)
    print(f'{len(a)}, sys.getsizeof(a) = {sys.getsizeof(a)}')

b = set()
for j in letters:
    b.add(j)
    print(f'{len(b)}, sys.getsizeof(b) = {sys.getsizeof(b)}')

c = dict()
for k in letters:
    c[k] = k
    print(f'{len(c)}, sys.getsizeof(c) = {sys.getsizeof(c)}')

"""
超额分配机制：
    申请新内存时并不是按需分配的，而是多分配一些，
    因此当再添加少量元素时，不需要马上去申请新内存

非均匀分配机制：
    三类对象申请新内存的频率是不同的，
    而同一类对象每次超额分配的内存并不是均匀的，
    而是逐渐扩大的
"""

# 3、列表不等于列表

# 静态创建对象
set_1 = {1, 2, 3, 4}
set_2 = {1, 2, 3, 4, 5}
dict_1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
dict_2 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}

sys.getsizeof(set_1)  # 224
sys.getsizeof(set_2)  # 736
sys.getsizeof(dict_1) # 240
sys.getsizeof(dict_2) # 368

# 在元素个数相等时，静态创建的集合/字典占用的内存跟动态扩容时完全一样

list_1 = ['a', 'b']
list_2 = ['a', 'b', 'c']
list_3 = ['a', 'b', 'c', 'd']
list_4 = ['a', 'b', 'c', 'd', 'e']

sys.getsizeof(list_1)  # 80
sys.getsizeof(list_2)  # 88
sys.getsizeof(list_3)  # 96
sys.getsizeof(list_4)  # 104

# 在元素个数相等时，静态创建的列表所占的内存有可能小于动态扩容时的内存！

# 4、削减元素并不会释放内存

import sys
a = [1, 2, 3, 4]
sys.getsizeof(a) # 初始值：96
a.append(5)      # 扩充后：[1, 2, 3, 4, 5]
sys.getsizeof(a) # 扩充后：128
a.pop()          # 缩减后：[1, 2, 3, 4]
sys.getsizeof(a) # 缩减后：128

# 如代码所示，列表在一扩一缩后，虽然回到了原样，
# 但是所占用的内存空间可没有自动释放啊。其它的可变对象同理。

# 5、空字典不等于空字典

# 使用 pop() 方法，只会缩减可变对象中的元素，但并不会释放已申请的内存空间。

# 还有个 clear() 方法，它会清空可变对象的所有元素，让我们试试看吧：

import sys
a = [1, 2, 3]
b = {1, 2, 3}
c = {'a':1, 'b':2, 'c':3}

sys.getsizeof(a) # 88
sys.getsizeof(b) # 224
sys.getsizeof(c) # 240

a.clear()        # 清空后：[]
b.clear()        # 清空后：set()
c.clear()        # 清空后：{}，也即 dict()
# 调用 clear() 方法，我们就获得了几个空对象。

# 在第一小节里，它们的内存大小已经被查验过了。（前面说过会考的，请默写 回看下）

# 但是，如果这时再去查验的话，你会惊讶地发现，这些空对象的大小跟前面查的并不完全一样！

# 承接前面的清空操作：
sys.getsizeof(a) # 64
sys.getsizeof(b) # 224
sys.getsizeof(c) # 72


# 空列表与空元组的大小不变，然而空字典（72）竟然比前面的空字典（240）要小很多！
# 也就是说，列表与元组在清空元素后，回到起点不变初心，然而，
# 字典这家伙却是“赔了夫人又折兵”，不仅把“吃”进去的全吐出来了，还把自己的老本给亏掉了！





