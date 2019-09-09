import urllib.request

from lxml import etree

from itertools import product

def parse(url):
    request = urllib.request.Request(url)
    resp = urllib.request.urlopen(request)
    text = resp.read().decode("gbk")

    selector = etree.HTML(text, etree.HTMLParser())

    data_localtions = selector.xpath("//div[@id='page_left']/table//td/strong/a/text()")
    data_urls = selector.xpath("//div[@id='page_left']/table//td/strong/a/@href")
    return data_localtions, data_urls

def parse_1(urls):
    data_street_urls = list()
    for url in urls:
        request = urllib.request.Request('http://www.tcmap.com.cn' + url)
        resp = urllib.request.urlopen(request)
        try:
            text = resp.read().decode("gbk")
        except UnicodeDecodeError:
            continue
        selector1 = etree.HTML(text, etree.HTMLParser())

        # data_streets = selector1.xpath("//div[@id='page_left']//table//td[@align='center']//a/text()")
        data_street_url = selector1.xpath("//div[@id='page_left']//table//td[@align='center']//a/@href")
        data_street_urls.append(data_street_url)
    return data_street_urls

def parse_2(urls):
    data_village_urls = list()
    for url in urls:
        request = urllib.request.Request('http://www.tcmap.com.cn' + url)

        resp = urllib.request.urlopen(request)
        try:
            text = resp.read().decode("gbk")
        except UnicodeDecodeError:
            continue
        selector2 = etree.HTML(text, etree.HTMLParser())

        # data_villages = selector2.xpath("//div[@id='page_left']//table//td[@align='center']//a/text()")
        data_village_url = selector2.xpath("//div[@id='page_left']//table//td[@align='center']//a/@href")
        data_village_urls.append(data_village_url)
    return data_village_urls

def parse_3(urls):
    datas = list()
    for url in urls:
        request = urllib.request.Request('http://www.tcmap.com.cn' + url)
        resp = urllib.request.urlopen(request)
        try:
            text = resp.read().decode("gbk")
        except UnicodeDecodeError:
            continue
        selector3 = etree.HTML(text, etree.HTMLParser())

        data = selector3.xpath("//div[@id='page_left']//h1/text()")
        datas.append(data)
    return datas


if __name__ == '__main__':

    with open('data_bj_plot.tsv','w',encoding='utf-8') as fp:
        url = "http://www.tcmap.com.cn/beijing/"
        data1, data2 = parse(url)

        data_street_urls = parse_1(data2)
        # print(len(data_street_urls))
        all_list = list()
        for l in data_street_urls:
            data_village_urls = parse_2(l)
            all_list.append(data_village_urls)
        # print(all_list)

        # print('---------------------------------------------')
        all_lists = list()
        for list_1 in all_list:
            # print(list_1)
            for list_2 in list_1:
                # print('-------------------------------------')
                # print(list_2)
                for u in list_2:
                    print('-------------------------------------------')
                    print(u)

                    request = urllib.request.Request('http://www.tcmap.com.cn' + u)
                    resp = urllib.request.urlopen(request)
                    try:
                        text = resp.read().decode("gbk")
                    except UnicodeDecodeError:
                        continue
                    selector3 = etree.HTML(text, etree.HTMLParser())

                    data = selector3.xpath("//div[@id='page_left']//h1/text()")
                    fp.write(data[0]+'\n')


