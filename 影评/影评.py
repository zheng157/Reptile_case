import requests
import csv
from lxml import etree
from itertools import zip_longest

def get_data(p, csv_writer):
    url = f'https://filmarks.com/movies/85106?page={p}'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=header)
    print(response.cookies)
    response = requests.get(url, headers=header).content
    xp = etree.HTML(response)

    div_elements = xp.xpath('//div[@class="p-mark__review"]')
    texts = [''.join(element.xpath('.//text()')).strip() for element in div_elements]
    scores = xp.xpath('//div[@class="c-media__content"]/div/div[2]/text()')
    times = xp.xpath('//div[@class="c-media__content"]/time/@datetime')
    likes = xp.xpath('//div[@class="c-reactions__button c-reactions__button--likes"]/span/text()')
    
    for text, score, time, like in zip_longest(texts, scores, times, likes, fillvalue=''):
        dti = {
        '影评内容': text,
        '评价时间': time,
        '评分': score,
        '点赞': like
    	}
        print(dti)
        csv_writer.writerow(dti)


# 假设我们在函数外部需要调用该函数并将结果写入CSV文件
if __name__ == "__main__":
    with open('影评.csv', 'a', encoding='utf-8', newline='') as f:
        csv_writer = csv.DictWriter(f, fieldnames=['影评内容', '评价时间', '评分', '点赞'])
        csv_writer.writeheader()
        for i in range(1, 405):
            get_data(i, csv_writer)  # 传递csv_writer给get_data函数