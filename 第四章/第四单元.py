import json

import requests

r = requests.get("https://api.bilibili.com/x/web-show/res/locs?pf=0&ids=3449").content.decode('utf-8')
a1 = json.loads(r)
a2 = a1["data"]["3449"]
# print(a1)
a = 20
for a3 in a2:
    a4 = a3["pic"]
    a5 = a3["name"]
    with open("{}.jpg".format(a),"wb") as f:
        f.write(requests.get(a4).content)
        a += 1
        print("下载 %s 完成" % a)
    # print(a4,",",a5)
