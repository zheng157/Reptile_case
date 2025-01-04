import random
import requests
from lxml import etree
import ddddocr
import openpyxl
import logging
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import json,time
from selenium.webdriver.chrome.options import Options


def getVerifyimagepage():
    # 获取验证码图片
    api = 'http://www.santostang.com/wp-admin/admin-ajax.php?captcha_code=7470'

    try:
        res = requests.get(api)
        with open('img.jpg', 'wb') as img:
            img.write(res.content)
    except Exception as e:
        print(e)

def imgRecognition(img):
    # 识别验证码
    try:
        ocr = ddddocr.DdddOcr()
        with open(img, 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        return res
    except:
        return None

def cookie_get():
    sou  = '1520'
    user = '15360128470'
    password = '1465852'
    # 配置选项
    options = Options()

    # 模拟浏览器登录
    options.add_experimental_option('detach', True)

    # 实现规避检测
    options.add_experimental_option('excludeSwitches', ['enable-automation'])

    # 初始化浏览器
    driver = webdriver.Chrome(options=options)
    # 使打开的屏幕最大化
    driver.maximize_window()
    driver.get('https://gg19.irobotbox.com/Manager/Login.aspx')

    x1, y1 = 1584, 466  # 左上角坐标
    x2, y2 = 1674, 498  # 右下角坐标

    # 获取整个页面截图
    screenshot_path = 'D:\pycharm\homework\爬虫案例\screenshot.png'
    driver.save_screenshot(screenshot_path)

    # 截取指定区域
    im = Image.open(screenshot_path)
    region = im.crop((x1, y1, x2, y2))

    # 保存截图
    cropped_path = 'D:\pycharm\homework\爬虫案例\img.jpg'
    region.save(cropped_path)

    driver.find_element(By.XPATH,"//input[@name='TextCustomerID']").send_keys(sou)
    driver.find_element(By.XPATH,"//input[@name='TextAdminName']").send_keys(user)
    driver.find_element(By.XPATH,"//input[@name='TextPassword']").send_keys(password)
    # verification_code = driver.find_element(By.XPATH, '//img[@id="captchaImage"]').get_attribute('src')  # 验证码url
    verification_codes = imgRecognition(img =cropped_path)
    print(verification_codes)
    driver.find_element(By.XPATH, "//input[@id='txtValidate']").send_keys(verification_codes)
    driver.find_element(By.XPATH, "//input[@id='submit']").click()
    time.sleep(5)
    driver.get('https://gg19.irobotbox.com/IrobotBox/WareHouse/WareHouseProductListV2.aspx?IsKeywordLike=false&Or derBy=UpdateTime%20DESC%2CID%20DESC&IsShowStock=0&PageSize=20&WareHouseIDs=2%2C-1100000&SearchType=1&BatchSearchType=1&KCType=0&NumSearchType=0&HistoryInSearchType=0&HistoryOutSearchType=0')
    time.sleep(2)

    cookie_items = driver.get_cookies()
    for cookie_item in cookie_items:
        post = {}
        post[cookie_item['name']] = cookie_item['value']

        cookie_str = json.dumps(post)
        time.sleep(3)
        with open('D:\文件加解密\各平台账号与密码\cookie.txt', 'w+', encoding='utf-8') as f:
            f.write(cookie_str)

def req():
    url = 'https://gg19.irobotbox.com/IrobotBox/WareHouse/WareHouseProductListV2.aspx?IsKeywordLike=false&OrderBy=UpdateTime%20DESC%2CID%20DESC&IsShowStock=0&PageSize=20&WareHouseIDs=2%2C-1100000&SearchType=1&BatchSearchType=1&KCType=0&NumSearchType=0&HistoryInSearchType=0&HistoryOutSearchType=0'
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"}

    with open('D:\文件加解密\各平台账号与密码\cookie.txt', 'r', encoding='utf-8') as f:

        cookie = f.read()

        cookies = json.loads(cookie)

        res = requests.get(url=url, cookies=cookies,headers = header)
        print(res.text)

if __name__ == '__main__':
    cookie_get()
    req()

