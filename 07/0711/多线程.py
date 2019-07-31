import threading
import os,time

lock = threading.Lock()
lock.acquire() # 申请加锁
lock.release() # 去锁
def say_hello(name):
    time.sleep(1)
    print("{} say hello world on {}!".format(name,os.getpid()))

def main():
    # name_list = ['Bob','Jack','Jone','Mike','David','Messi','James','Hardn','Ricardo','Asule']
    for i in range(100000):
        thread = threading.Thread(target=say_hello,args=(i,))
        thread.start()
main()
# print(threading.activeCount())
# print(threading.currentThread())
# print(threading.enumerate())
