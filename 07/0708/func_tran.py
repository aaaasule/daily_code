import time,os,random
from multiprocessing import Pool, Process

def comm():
    pass


def handle(a, b):
    t_start = time.time()
    c = a + b
    t_end = time.time()
    print(c, "执行时间为：{}".format(t_end - t_start))
    return c


if __name__ == '__main__':
    po = Pool(3)
    for i in range(0, 3):
        po.apply_async(handle, (i, 2))
    print("------start-------")
    po.close()
    po.join()
    print("-----------end------------")
