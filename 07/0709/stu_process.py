import time
import random
import os
from multiprocessing import Process,Pool
"""
# 开启进程的方法一
def piao(name):
    print('{} piaoing'.format(name))
    time.sleep(random.randrange(1,5))
    print('{} piaoing'.format(name))

if __name__ == "__main__":
    p1 = Process(target=piao,args=('agon',))
    p2 = Process(target=piao,args=('alex',))
    p3 = Process(target=piao, args=('wang',))
    p4 = Process(target=piao,args=('zhang',))

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print("主线程")
"""

"""
#开进程的方法二:
class Piao(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def run(self):
        print('%s piaoing' %self.name)
        time.sleep(random.randrange(1,5))
        print('%s piao end' %self.name)
if __name__ == "__main__":
    p1=Piao('egon')
    p2=Piao('alex')
    p3=Piao('wang')
    p4=Piao('zhang')

    p1.start() #start会自动调用run
    p2.start()
    p3.start()
    p4.start()
    print('主线程')
"""
def worker(msg):
    t_start = time.time()
    print("{} 开始执行，进程号为{}".format(msg,os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕，耗时{}".format(t_stop-t_start))

if __name__ == "__main__":
    po = Pool(3)
    for i in range(0,10):
        po.apply_async(worker,(i,))
    print("----start----")
    po.close()
    po.join()
    print("-----------------end-----------------------")