from selenium import webdriver
from selenium.webdriver.common.by import By
import time,csv



def drop_down():  #下拉的方法
    for x in range(1,12,2):
        time.sleep(1)
        j = x / 9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


# seLenium 模拟人的行为 获取数据内容
driver = webdriver.Chrome()
driver.get('https://search.1688.com/company/pc/factory_search.html?keywords=%C4%CF%BE%A9&spm=')
drop_down()

# product_list = driver.find_elements(By.XPATH, '//div[@class="main-content"]')
# print(len(product_list))
# for i in product_list:







