# -*- coding:utf-8 -*-
from multiprocessing import Process,Queue,Pipe



def say_hello(con_a):

    print('我在子进程发送了数据：{}'.format(con_a.recv()))


if __name__ == '__main__':
    # 建立管道
    con_a,con_b = Pipe()

    p = Process(target=say_hello,args=(con_a,))
    p.start()

    con_b.send("啦啦啦，德玛西亚")