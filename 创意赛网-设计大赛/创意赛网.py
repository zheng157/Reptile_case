import urllib.parse
from lxml import etree
import requests,csv

def a1():
    urls =[]
    name_wg = input('请输入你想要获取数据:')
    a1 = int(input('请输入下载页码'))
    a2 = int(input('请输入结束页码'))

    for x in range(a1,a2+1):
        url_http = f'http://chuangyisai.com/search/index/page-{x}.html?'
        data ={
            'keyword': str(name_wg),
            'model':2
        }
        name = urllib.parse.urlencode(data)
        url_name = url_http + name
        urls.append(url_name)
    return urls

def a2(urls):
    with open('创意赛网.csv', 'a', encoding='utf-8', newline='') as f:
        csv_writer = csv.DictWriter(f, fieldnames=['名城', '连接', '时间'])
        if f.tell() == 0:
            csv_writer.writeheader()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        for url in urls:
            request = requests.get(url,headers=headers).content.decode('utf-8')
            res = etree.HTML(request)

            name = res.xpath('//ul[@class="competition-list clearfix"]/li/span[1]/a[2]/text()')
            urls = res.xpath('//ul[@class="competition-list clearfix"]/li/span[1]/a[2]/@href')
            time = res.xpath('//ul[@class="competition-list clearfix"]/li/span[2]/text()')
            for name, urls, time in zip(name, urls, time):
                if time and time != [' ']:
                    name = ''.join(name)
                    time = ''.join(time)
                    urls = 'http://chuangyisai.com'+''.join(urls)

                    dti = {
                        '名城': name,
                        '连接': url,
                        '时间': time,
                    }
                    csv_writer.writerow(dti)
                    print(name, time, urls)
    f.close()

        # wg = res.xpath('//ul[@class="competition-list clearfix"]/li')
        # print(len(wg))
        # for wgs in wg:
        #     name = wgs.xpath('./span[1]/a[2]/text()')
        #     urls = wgs.xpath('./span[1]/a[2]/@href')
        #     time = wgs.xpath('./span[2]/text()')
        #     if time and time != [' ']:
        #         name = ''.join(name)
        #         time = ''.join(time)
        #         urls = 'http://chuangyisai.com'+''.join(urls)
        #         print(name,time,urls)


if __name__ == '__main__':
    urls=a1()
    a2(urls)