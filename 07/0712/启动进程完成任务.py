from multiprocessing import Process
import time

def saygoodbye():
    while True:
        print("good bye!")
        time.sleep(1)

def sayhello():
    while True:
        print("hello world!")
        time.sleep(2)

if __name__ == "__main__":
    process_bye = Process(target=saygoodbye)
    process_bye.start()

    process_hello = Process(target=sayhello)
    process_hello.start()
