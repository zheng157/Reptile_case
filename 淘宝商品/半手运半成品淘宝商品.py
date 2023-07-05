from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


f = open('京东耳机.csv', 'a', encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=[
        '商品名称',
        '商品价格',
        '店铺名',
        '地址',])
csv_writer.writeheader()


def drop_down():  #下拉的方法
    for x in range(1,12,2):
        time.sleep(1)
        j = x / 9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


driver = webdriver.Chrome()
driver.get('https://www.taobao.com/')

driver.find_element(By.XPATH, '//*[@id="q"]').send_keys("手机")
driver.find_element(By.XPATH, '//*[@id="J_TSearchForm"]/div[1]/button').click()
driver.implicitly_wait(5)

try:
    login_popup = driver.find_element(By.XPATH, '//*[@id="login"]/div[1]/i').click()
    driver.implicitly_wait(5)
    drop_down()
except:
    pass



product_list = driver.find_elements(By.XPATH,'//div[@class="grid g-clearfix"]//div[@class="ctx-box J_MouseEneterLeave J_IconMoreNew"]')

for product in product_list:

    name_element = product.find_element(By.XPATH, './/a[@id]')#名称
    name = name_element.text

    price_element = product.find_element(By.XPATH, './/div[@class="price g_price g_price-highlight"]/strong') #价格
    price = price_element.text

    shops = product.find_element(By.XPATH, './div[3]/div/a/span[2]')  # 店铺名
    shop = shops.text

    sites = product.find_element(By.XPATH, './div[3]/div[@class="location"]')  # 地址
    site = sites.text
    dti = {
        '商品名称': name,
        '商品价格': price,
        '店铺名': shop,
        '地址': site,

    }
    csv_writer.writerow(dti)
    print(name,price,shop,site)
