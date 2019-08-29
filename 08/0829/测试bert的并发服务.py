
import requests
from multiprocessing import Process,Pool,cpu_count


def post_bert():
    url = "http://192.168.50.131:8080/encode"

    data = {"id": 14, "texts": ["我想查话费", "我办一个五十元流量加油包"], "is_tokenized": False}

    resp = requests.post(url, json=data)

    print(resp.json())
    return resp.json()

if __name__ == "__main__":

    # 获取cpu核心数
    cpu_num = cpu_count()

    # 创建进程池
    pp = Pool(cpu_num)

    for i in range(3):
        pp.apply(func=post_bert())

    pp.close()
    pp.join()


