# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 0029 14:02
# @Author  : Zhang
# @File    : ansyncandawait.py
import asyncio
import random
from time import sleep


class Potato:
    @classmethod
    def make(cls, num, *args, **kwargs):
        potatos = []
        for i in range(num):
            potatos.append(cls.__new__(cls, *args, **kwargs))
        return potatos

all_potatos = Potato.make(5)
print(all_potatos)

# def take_potatos(num):
#     count = 0
#     while True:
#         if len(all_potatos) == 0:
#             sleep(1)
#         else:
#             potato = all_potatos.pop()
#             yield potato
#             count += 1
#             if count == num:
#                 break

# def buy_potatos():
#     bucket = []
#     for p in take_potatos(50):
#         bucket.append(p)

async def take_potatos(num):
    count = 0
    while True:
        if len(all_potatos) == 0:
            await ask_for_potato()
        potato = all_potatos.pop()
        yield potato
        count += 1
        if count == num:
            break


async def ask_for_potato():
    await asyncio.sleep(random.random())
    all_potatos.extend(Potato.make(random.randint(1, 10)))
