import requests
import urllib.parse
from lxml import etree


NEWS_DATA = []


def url(i):
    if (i == 0):
        url = "https://gxcme.edu.cn/xwdt/jdyw.htm"
    else:
        url = 'https://gxcme.edu.cn/xwdt/jdyw/{}.htm'.format(i)
    return url


def smjn(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    r = requests.get(url=url,headers = headers).content.decode('utf-8')
    res = etree.HTML(r)
    mane = res.xpath('//div[@class="ej_right_new"]/ul/li/a/text()')
    url2 = res.xpath('//div[@class="ej_right_new"]/ul/li/a/@href')

    for i in url2:
        ulr3 = 'https://gxcme.edu.cn/'+i[3:]
        re = requests.get(url = ulr3,headers = headers).content.decode('utf-8')
        res = etree.HTML(re)
        mwpw = res.xpath('//div[@class="v_news_content"]/p/span/text()')

        if not mwpw:
            mwpw = '无内容'

        NEWS_DATA.append({
            '标题': mane[0],
            '内容': mwpw
        })

    print(NEWS_DATA)



if __name__ == '__main__':
    i = 1
    for i in range(0,11):
        url2 = url(i)
        smjn(url2)


