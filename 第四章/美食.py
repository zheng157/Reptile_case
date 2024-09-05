import json
import requests

r = requests.get("https://api.huaban.com/search?q=%E5%8F%91%E7%8E%B0&sort=all&category=food_drink&per_page=20&page=2&hide_other_count=1https://api.huaban.com/search?q=%E5%8F%91%E7%8E%B0&sort=all&category=food_drink&per_page=20&page=2&hide_other_count=1").content
r = r.decode('utf-8')

# print(r)
a1 = json.loads(r)
a=1
a2 = a1["pins"]
n =0
for a3 in a2:
    a4 = a3['file']['key']
    a5 = "https://gd-hbimg.huaban.com/"+a4
    with open('{}.jpg'.format(n), "wb") as f:
        f.write(requests.get(a5).content)
        n += 1
        print("下载 %s 完成" % a4)
