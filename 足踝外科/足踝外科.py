import requests,csv
from lxml import etree




f = open('足踝外科.csv', 'a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['标题','内容',])
csv_writer.writeheader()

def a(ii):

    url = f'https://www.120ask.com/list/zhwk/over/{ii}/'

    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    r = requests.get(url,headers=header).content
    xp = etree.HTML(r)
    si = xp.xpath('//div/ul[@class="clears h-ul3"]/li//a')
    for i in si:
        url2 = "https:"+ i.xpath('@href')[0]
        r2 = requests.get(url2, headers=header).content
        xp2 = etree.HTML(r2)
        try:
            mina = xp2.xpath('//*[@id="d_askH1"]/text()')[0]
        except IndexError as e:
            mina = ''

        try:
            content = xp2.xpath('//div[@class="b_answerli"]/div[2]//div[@class="crazy_new"]/p/text()')[0]
        except IndexError as e:
            content = ''
        dti = {
            '标题':mina,
            '内容':content.replace('\xa0', "")
        }
        print(dti)
        csv_writer.writerow(dti)

for ii in range(99,200):
    a(ii)
