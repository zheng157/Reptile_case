from selenium import webdriver
from selenium.webdriver.common.by import By
import time,csv


def drop_down():  #下拉的方法
    for x in range(1,12,2):
        time.sleep(1)
        j = x / 9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


def a1():
    driver = webdriver.Chrome()
    driver.get('https://guba.eastmoney.com/list,usbaba_1.html')  # 访问一个网址 打开浏览器 打开网址
    driver.implicitly_wait(5)
    drop_down()

    product_list = driver.find_elements(By.XPATH, '//table/tbody[@class="listbody"]/tr')
    print(len(product_list))
    for product in product_list:
        connects = product.find_element(By.XPATH, './td[3]/div/a')
        connect = connects.get_attribute('href')  # 连接
    return connect



if __name__ == '__main__':
    connect = a1()
    print(connect)
