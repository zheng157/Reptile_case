from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import json,time


def cookie_get():
    user = '745623d2cac2424ca18034bc4dfe1e0b'
    password = 'Zheng123@'

    driver = webdriver.Chrome()
    driver.get('https://app113657.eapps.dingtalkcloud.com/srm/order/OrderBuyHeadList')
    driver.find_element(By.XPATH,"//div[@class='ant-form-item-control']//input[@type='text']").send_keys(user)
    driver.find_element(By.XPATH, "//div[@class='ant-form-item-control']//input[@type='password']").send_keys(password)
    driver.find_element(By.XPATH, "//div[@class='ant-form-item-control']//button").click()
    driver.get('https://app113657.eapps.dingtalkcloud.com/srm/order/OrderBuyHeadList')
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
    url = 'https://app113657.eapps.dingtalkcloud.com/srm/order/OrderBuyHeadList'
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"}

    with open('D:\文件加解密\各平台账号与密码\cookie.txt', 'r', encoding='utf-8') as f:

        cookie = f.read()

        cookies = json.loads(cookie)

        res = requests.get(url=url, cookies=cookies,headers = header)
        print(res.text)

if __name__ == '__main__':
    cookie_get()