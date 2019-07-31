import requests
from lxml import etree

url_loca = "http://www.tcmap.com.cn/"


# xpath  ----   //td[@width='748']//div[@id='list110']/a/text()

def parse_loca(url, loca_list):
    resp_loca = requests.get(url=url).content.decode('gbk')
    dom_tree_loca = etree.HTML(resp_loca)
    data_loca = dom_tree_loca.xpath("//td[@width='748']//div[@id='list110']/a/text()")
    loca_list.extend(data_loca)
    print(len(loca_list))
    print(loca_list)
def parse_loca_2(loca_list,url):

    resp_loca_2 = requests.get(url=url).content.decode('gbk')
    dom_tree_loca_2 = etree.HTML(resp_loca_2)
    data_loca_2 = dom_tree_loca_2.xpath("//div[@id='pagebody']//table[@width='738']//strong/a[@class='blue']/text()")
    loca_list.extend(data_loca_2)
    return loca_list


def parse_loca_url(url,url_list):
    resp_loca_url = requests.get(url=url).content.decode('gbk')
    dom_tree_loca_url = etree.HTML(resp_loca_url)
    data_loca_url = dom_tree_loca_url.xpath("//td[@width='748']//div[@id='list110']/a/@href")
    print(data_loca_url)
    for i in data_loca_url:
        i = 'http://www.tcmap.com.cn' + i
        url_list.append(i)
    print(url_list)
    return url_list


if __name__ == "__main__":
    loca_list = list()
    parse_loca(url=url_loca,loca_list=loca_list)
    url_list = list()
    url_list = parse_loca_url(url=url_loca,url_list=url_list)
    print(url_list)
    # http://www.tcmap.com.cn/beijing/dongchengqu.html
    url_pop_list = ["http://www.tcmap.com.cn/beijing/changping.html","http://www.tcmap.com.cn/tianjin/hebeiqu.html","http://www.tcmap.com.cn/fujian/fuzhou.html","http://www.tcmap.com.cn/jiangxi/jingdezhen.html","http://www.tcmap.com.cn/shandong/dezhou.html","http://www.tcmap.com.cn/guangdong/yunfushi.html","http://www.tcmap.com.cn/hainan/wuzhishan.html","http://www.tcmap.com.cn/chongqing/wanzhouqu.html","http://www.tcmap.com.cn/chongqing/shapingbaqu.html","http://www.tcmap.com.cn/sichuan/mianyang.html","http://www.tcmap.com.cn/sichuan/aba.html",
                    "http://www.tcmap.com.cn/sichuan/ganzi.html","http://www.tcmap.com.cn/guizhou/kaili(qiandongnanzhou).html","http://www.tcmap.com.cn/shanxi/xian.html","http://www.tcmap.com.cn/taiwan/pingdong.html"
                    ]
    for url_pop in url_pop_list:
        url_list.remove(url_pop)
    for i in url_list:
        print(i)
        data_loca_list = parse_loca_2(loca_list=loca_list,url=i)
    with open("data_new.txt", 'a+') as f:
        for loca in data_loca_list:
            f.write(loca + " ns\n")
