
# http://192.168.50.131:8080/encode?id=12&texts=我想查话费&is_tokenized=False

from time import sleep
import os
from multiprocessing import Process,Pool,cpu_count
import requests
import json
import urllib.request

data = {
    'id': 12,
    'texts': '我想查话费',
    'is_tokenized': False
}

params = json.dumps(data)

def post_bert():

    resp = requests.post('http://192.168.50.131:8080/encode')
    print(resp.json())

resp = requests.post("http://192.168.50.131:8080/encode",data=params)

print(resp)

# texts = []
#
# if __name__ == '__main__':
#
#     cpu
    # cpu_num = cpu_count()
    # print(cpu_num)

    # pp = Pool(cpu_num)
    # for i in range(20):
    #     pp.apply_async(func=post_bert(),args=(os.getpid(),))
    #
    # pp.close()
    #
    # pp.join()