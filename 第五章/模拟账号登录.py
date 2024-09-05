
import tesserocr
from selenium import webdriver
from selenium.webdriver.common.by import By
from io import BytesIO
from PIL import Image
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException
from retrying import retry

@retry(stop_max_attempt_number=10,retry_on_result=lambda x: x is False)
def login():
    browser.get('https://captcha7.scrape.center/')
    browser.find_element(By.CSS_SELECTOR,"#app > div:nth-child(2) > div > div > div > div > div > form > div:nth-child(2) > div > div > input").send_keys("admin")
    browser.find_element(By.CSS_SELECTOR,"#app > div:nth-child(2) > div > div > div > div > div > form > div:nth-child(3) > div > div > input").send_keys("admin")
    captcha = browser.find_element(By.ID,"captcha")


    image = Image.open(BytesIO(captcha.screenshot_as_png))
    captcha_reslut = tesserocr.image_to_text(image)
    print("captcha_reslut",captcha_reslut)
    captcha_reslut = re.sub('[^A-Za-z0-9]', '',captcha_reslut)
    print("captcha_reslut", captcha_reslut)
    browser.find_element(By.CSS_SELECTOR,"#app > div:nth-child(2) > div > div > div > div > div > form > div:nth-child(4) > div > div > div.el-col.el-col-15 > div > input").send_keys(captcha_reslut)
    browser.find_element(By.CSS_SELECTOR,"#app > div:nth-child(2) > div > div > div > div > div > form > div:nth-child(5) > div > button").click()
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[contains(., "登录成功")]')))
        time.sleep(10)
        browser.close()
        return True
    except TimeoutException:
        return False




if __name__ == '__main__':
    browser = webdriver.Chrome()
    flag = login()
