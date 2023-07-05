import requests
import urllib.request
from bs4 import BeautifulSoup
def aa(i):
    if(i==1):
        url = "http://www.bizhi360.com/desk/index.html"
    else:
        url ='http://www.bizhi360.com/meinv/list_{}.html'.format(i)
    return url

def bb(url):
    b1 = requests.get(url).content.decode(' utf -8')
    b2 = BeautifulSoup(b1, 'html.parser')
    b3 = b2.select('.pic-list>ul>li>a')
    for b3 in b3:
        b4 = b3['href']
        b5 = 'http://www.bizhi360.com'+ b4
        c1 = requests.get(b5).content.decode(' utf -8')
        c2 = BeautifulSoup(c1, 'html.parser')
        c3 = c2.select('.article>figure>a')[0]
        c4 = c3['href']
        c5 = c3['title']
        urllib.request.urlretrieve(url=c4, filename='./相片/' + c5 + '.jpg')
        print("下载"+c5+"完成")

if __name__ == '__main__':
    i = 1
    for i in range(1,11):
        url =aa(i)
        bb(url)
