
from time import sleep
import os
from multiprocessing import Process,Pool,cpu_count

def say_hello(name):
    print("I am {}".format(name))

if __name__ == '__main__':

    # cpu
    cpu_num = cpu_count()
    print(cpu_num)
    #
    pp = Pool(cpu_num)
    for i in range(20):
        pp.apply_async(func=say_hello,args=(os.getpid(),))

    pp.close()

    pp.join()