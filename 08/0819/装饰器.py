# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 0019 14:03
# @Author  : Zhang
# @File    : 装饰器.py

import time


# 1 hello  装饰器
def decoretor(func):
    def wrapper(*args,**kwargs):
        func()
    return wrapper()


# @decoretor
# def function():
#     print("hello,decorator")

# 2 日志装饰器
def logger(func):
    def wrapper(*args,**kwargs):
        print('主人，我准备执行：{}函数了：'.format(func.__name__))

        func(*args,**kwargs)

        print("主人，我执行完了")
    return wrapper
@logger
def add(x,y):
    print('{} + {} = {}'.format(x,y,x+y))

# add(14,14)

# 3 时间装饰器

def timer(func):
    def wrapper(*args,**kwargs):
        t1 = time.time()
        func(*args,*kwargs)
        t2 = time.time()
        t = t2 - t1
        print("函数执行一共花费了：{}的时间".format(t))
    return wrapper

@timer
def want_sleep():

    time.sleep(10)

# 4 带参数的装饰器

def say_hello(contry):
    def wrapper(func):
        def deco(*args,**kwargs):
            if contry == "china":
                print("你好")
            elif contry == "American":
                print("hello")
            else:
                return

            func()
        return deco
    return wrapper

@say_hello("china")
def xiaoming():
    pass

@say_hello("American")
def jack():
    pass

# xiaoming()
#
# jack()

# 5 不带参数的类装饰器
class logger(object):

    def __init__(self,func): # 接收被装饰函数
        self.func = func

    def __call__(self, *args, **kwargs): # 实现装饰逻辑
        print("[INFO]：the function {func}() is running ... " \
              .format(func=self.func.__name__))
        return self.func(*args,**kwargs)

@logger
def say(something):
    print("say: {}!".format(something))

# say("hello")

# 6 带参数的类装饰器

class logger(object):

    def __init__(self,level='INFO'): # 不在接收被装饰函数，而是接收传入参数
        self.level = level

    def __call__(self, func): # 接收被装饰函数  实现装饰逻辑

        def wrapper(*args,**kwargs):

            print("[{level}]:the function {func}() is running..."\
                  .format(level=self.level,func=func.__name__))
            func(*args,**kwargs)
        return wrapper

@logger(level="WRANING")
def say(something):
    print("say:{something}！".format(something=something))

say("hello")

# 7 使用偏函数和类实现装饰器

# ...

# 10 内置装饰器 property

"""
用@property装饰过的函数，会将一个函数定义成一个属性，
属性的值就是该函数return的内容。
同时，会将这个函数变成另外一个装饰器。
"""




