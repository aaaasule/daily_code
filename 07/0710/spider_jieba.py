import requests
from lxml import etree

url_location = "http://www.tcmap.com.cn/" # xpath  ----   //td[@width='748']//div[@id='list110']/a
url_name = "http://www.resgain.net/mrdq.html"
url_jigou = ""

def parse_name(url,name_list):
    resp_name = requests.get(url=url).content.decode('utf-8')
    dom_tree_name = etree.HTML(resp_name)
    data_name= dom_tree_name.xpath("//div[@class='container']//h2/text()")

    print(type(data_name))
    name_list.extend(data_name)
    print(name_list)
def parse_name_url(url):
    resp_name_url = requests.get(url=url_name).content.decode('utf-8')
    dom_tree_name_url = etree.HTML(resp_name_url)
    data_name_url = dom_tree_name_url.xpath("//div[@class='row']//a[@target='_blank']/@href")
    return data_name_url


if __name__ == "__main__":
    name_url_list = parse_name_url(url=url_name)
    print(name_url_list)
    # for  i in name_url_list: # 拼接url
    #     i = i[:24] + "forum/cele.rhtml?page="
    #     print(i)
    # name_url_list_new = list()
    # for j in range(1,16):
    #     i = i + str(j)
    #     name_url_list_new.append(i)
    # print(name_url_list_new)

    # 解析html  写入txt
    name_list = list()
    for name_url in name_url_list:
        parse_name(url=name_url,name_list=name_list)
    print(name_list)
    with open('data_new.txt','w') as f:

        for name in name_list:
            f.write(name + ' nr\n')