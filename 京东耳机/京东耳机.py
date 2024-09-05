from selenium import webdriver
from selenium.webdriver.common.by import By
import time,csv


f = open('京东耳机.csv', 'a', encoding='utf-8',newline='')
csv_writer = csv.DictWriter(f,fieldnames=[
        '商品名称',
        '商品价格',
        '商品评价量',
        '店铺名',
        '标签',
        '商品链接',])
csv_writer.writeheader()


def drop_down():  #下拉的方法
    for x in range(1,12,2):
        time.sleep(1)
        j = x / 9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


# seLenium 模拟人的行为 获取数据内容
driver = webdriver.Chrome()
driver.get('https://www.jd.com/')#访问一个网址 打开浏览器 打开网址

#通过xpath语法在element(元素面板)里面查找 .key 某个标签数据 输入一个关键词 耳机
driver.find_element(By.XPATH, '//*[@id="key"]').send_keys('耳机')
driver.find_element(By.XPATH, '//*[@id="search"]/div/div[2]/button').click() ## 我到搜索按钮 进行点击
driver.implicitly_wait(5)   #隐式等待 等待网页数据加载完成5S 只要网页数据加载完成就会运行下面代码





def aa():

    product_list = driver.find_elements(By.XPATH, '//*[@id="J_goodsList"]/ul/li/div[@class="gl-i-wrap"]')
    # print(len(product_list))

    for product in product_list:
        # 通过XPath定位商品名称、价格,标签和链接
        name_element = product.find_element(By.XPATH, './div[@class="p-name p-name-type-2"]/a/em') #名称
        name = name_element.text.replace('\n','')

        price_element = product.find_element(By.XPATH, './div[@class="p-price"]/strong/i') #价格
        price = price_element.text

        evaluates = product.find_element(By.XPATH, './div[@class="p-commit"]/strong/a') #评价量
        evaluate = evaluates.text

        shops = product.find_element(By.XPATH, './div[@class="p-shop"]/span/a') #店铺名
        shop = shops.text

        link_element= product.find_element(By.XPATH, './div[@class="p-img"]/a') #链接
        link = link_element.get_attribute('href')

        icons = product.find_elements(By.XPATH, './div[@class="p-icons"]/i') #标签
        icon =[i.text for i in icons] # 列表推导式 ''.join 把列表转成字符串
        ico = ','.join(icon)

        dti = {
            '商品名称':name,
            '商品价格':price,
            '商品评价量':evaluate,
            '店铺名':shop,
            '标签':ico,
            '商品链接':link,
        }
        csv_writer.writerow(dti)
        print(name, price,evaluate,ico,shop,link)


for i in range(1,6):
    print(f'正在下载{i}页的内容')
    drop_down()
    time.sleep(1)
    aa() #下载数据的函数
    driver.find_element(By.XPATH, '//a[@class="pn-next"]').click() # 点击下一页
f.close()
driver.quit()