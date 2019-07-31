import threading

class MyThead(threading.Thread):

    def __init__(self,count,name):
        super(MyThead,self).__init__()
        self.count = count
        self.name = name

    def run(self):
        while self.count > 10:
            print("hello",self.name)
            self.count -= 1
