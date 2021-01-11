import time
import re
import function as fc
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
# options._arguments = ['disable-infobars']
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument("--start-maximized")
options.add_argument('--proxy-server=http://127.0.0.1:8080')  # 使用mitmdump避免被检测

driver = webdriver.Chrome(chrome_options=options)

driver.get("https://www.taobao.com/")
# 使用 selenium 显示等待
element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_link_text("我的淘宝"))

ActionChains(driver).move_to_element(element).perform()  # 使用perform() 模拟鼠标悬浮

WebDriverWait(driver, 10).until(lambda x: x.find_element_by_link_text("已买到的宝贝").is_displayed())

driver.find_element_by_link_text("已买到的宝贝").click()

element.click()



# obj = driver.find_element_by_xpath("//a[contains(text(),'已买到的宝贝')]")