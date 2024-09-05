import requests,csv
from lxml import etree

r = requests.get("http://www.redbull.com.cn/about/branch").content.decode('utf-8')

a1 = etree.HTML(r)
with open('红牛公司信息.csv', 'a', encoding='utf-8',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['公司名字', '地址', '邮箱', '电话'])
a2 = a1.xpath('//div[@class="con"]/ul/li')
for a3 in a2:
    a4 = a3.xpath('./h2/text()')[0]
    a5 = a3.xpath('./p[1]/text()')[0]
    a6 = a3.xpath('./p[2]/text()')[0]
    a7 = a3.xpath('./p[3]/text()')[0]
    print(a4,a5,a6,a7)
    with open('红牛公司信息.csv', 'a', encoding='utf-8',newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([a4, a5, a6, a7])


