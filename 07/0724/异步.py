# -*- coding:utf-8 -*-
import time
import asyncio
# from asyncore import loop
loop = asyncio.get_event_loop()

async def hello():
    asyncio.sleep(1)
    print('Hello World：{}'.format(time.time()))

def run():
    for i in range(5):
        loop.run_until_complete(hello())



if __name__ == '__main__':
    run()