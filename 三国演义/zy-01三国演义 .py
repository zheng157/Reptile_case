import requests
from bs4 import BeautifulSoup

ww1 = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }

ww2 = "https://www.shicimingju.com/book/sanguoyanyi.html"

ww3 = requests.get(url = ww2,headers = ww1).content

ww4= BeautifulSoup(ww3,'lxml')
ww5 = ww4.select('.book-mulu>ul>li')

b1 = open('三国.txt', 'w', encoding='utf-8')
for ww6 in ww5:
    ww7 = ww6.a.string
    ww8 = ww6.a["href"]
    ww9 = 'https://www.shicimingju.com' +ww8
    ww10 = requests.get(url=ww9, headers=ww1).content
    ww11 = BeautifulSoup(ww10, 'lxml')
    ww12 = ww11.find('div', class_='chapter_content')
    ww13 = ww12.text
    b1.write(ww7+":"+ww13+'\n')
    print('ok')
