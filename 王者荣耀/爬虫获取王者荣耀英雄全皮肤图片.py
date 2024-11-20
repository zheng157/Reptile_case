import requests
import json
import os
import time


def get_hero_info():
    # 英雄的全部信息的url
    hero_info = 'https://pvp.qq.com/web201605/js/herolist.json'
    # 获取英雄的全部信息
    response = requests.get(hero_info)
    # 转为字典格式
    hero_info_dict = json.loads(response.text)
    return hero_info_dict


def downloads_img():
    hero_info_dict = get_hero_info()
    for hero in hero_info_dict:
        # 获取单个英雄的名字
        hero_name = hero['cname']
        # 获取英雄的ID
        hero_num = hero['ename']
        # 图片保存的根路径
        hero_image_path = 'D:\\imgs\\' + hero_name
        # 创建文件夹
        os.mkdir(hero_image_path)
        print(hero_name + '皮肤正在下载....:')
        # 判断英雄是否有皮肤
        if 'skin_name' in hero:
            hero_skins = hero['skin_name']
            # 判断英雄皮肤个数是否大于1
            if '|' in hero_skins:
                # 将英雄的皮肤姓名以 | 分隔开
                hero_skin_list = hero_skins.split('|')
                # 英雄的皮肤个数
                hero_skin_count = len(hero_skin_list)
                for hero_skin_num in range(hero_skin_count):
                    # 英雄的皮肤名字
                    hero_skin_name = hero_skin_list[hero_skin_num]
                    # 英雄皮肤图片的url地址
                    hero_skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(
                        hero_num) + '/' + str(hero_num) + '-bigskin-' + str(hero_skin_num + 1) + '.jpg'
                    # 将图片转为字节形式
                    image_content = requests.get(hero_skin_url).content  # 请求url
                    # 保存图片
                    with open(hero_image_path + '\\' + hero_name + '-' + hero_skin_name + '.jpg', 'wb') as image:
                        image.write(image_content)
                    print("  【%s】皮肤下载完毕" % hero_skin_name)
        time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    downloads_img()
    end = time.time()
    print('共耗时' + str(end - start) + '秒')

