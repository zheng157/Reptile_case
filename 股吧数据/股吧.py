from selenium import webdriver
from selenium.webdriver.common.by import By
import time,csv

f = open('股吧.csv', 'a', encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=[
        '评论',
        '标题',
        '作者',
        '时间',])
csv_writer.writeheader()

def drop_down():  #下拉的方法
    for x in range(1,12,2):
        time.sleep(1)
        j = x / 9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


driver = webdriver.Chrome()
driver.get('https://guba.eastmoney.com/list,usbaba_685.html')#访问一个网址 打开浏览器 打开网址
driver.implicitly_wait(5)

def a1():
    product_list = driver.find_elements(By.XPATH, '//table/tbody[@class="listbody"]/tr')
    for product in product_list:
        # 通过XPath定位商品名称、价格,标签和链接
        comments = product.find_element(By.XPATH,'./td[2]/div')
        comment = comments.text #评论

        names = product.find_element(By.XPATH, './td[3]/div/a')
        name = names.text  #标题

        authors = product.find_element(By.XPATH, './td[4]/div/a')
        author = authors.text  # 作者

        times = product.find_element(By.XPATH, './td[5]/div')
        time = times.text  # 时间

        connects = product.find_element(By.XPATH, './td[3]/div/a')
        connect = connects.get_attribute('href') # 连接
        dti = {
            '评论': comment,
            '标题': name,
            '作者': author,
            '时间': time,
        }
        csv_writer.writerow(dti)
        print(comment,name,author,time)
for i in range(685,686):
    print(f'正在下载{i}页的内容')
    drop_down()
    time.sleep(1)
    a1() #下载数据的函数

    next_page = driver.find_element(By.XPATH, '//a[@class="nextp"]')
    driver.execute_script("arguments[0].click();", next_page)
    time.sleep(2)
driver.quit()