# 学号：20215102090065
# 姓名：郑艺

import requests
import json

n = 1
i = 1
for i in range(1,101):
    with  open('电影{}.txt'.format(i), 'w', encoding='utf-8') as b1:
            url = 'https://spa1.scrape.center/api/movie/{}'.format(i)
            a1 = requests.get(url).content.decode('utf-8')
            a2 = json.loads(a1)
            a5 = a2["name"]
            a6 = a2["cover"]
            a7 = a2["categories"]
            a8 = a2["published_at"]
            a9 = a2["minute"]
            a10 = a2["score"]
            a11 = a2["regions"][0]
            a12 = a2["drama"]
            a13 = "电影名：{} \n上映时间：{}  \n时长：{}分钟  \n评分：{} \n国家：{} \n剧情简介:\n    {}".format(a5,a8,a9,a10,a11,a12)
            b1.write(a13)
            a14 = requests.get(a6).content
            with open("图片{}.jpg".format(n), "wb") as b2:
                b2.write(a14)
                print("ok")
                n += 1
                i += 1

