import time
import re
from selenium import webdriver

options = webdriver.ChromeOptions()
# options._arguments = ['disable-infobars']  # 避免被检测
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument("--start-maximized")
options.add_argument('--proxy-server=http://127.0.0.1:8080')

driver = webdriver.Chrome(chrome_options=options)

driver.get("https://login.aliexpress.com/buyer.htm?spm=a2g1y.promotion-20181111.1000002.7.311f5e28ugMVc2&return=https%3A%2F%2Fwww.aliexpress.com%2Fstore%2F4282057%3Fspm%3D2114.10010108.0.0.433e2daaVKvagh&from=lighthouse&random=C3E91EFF317077B02C559F1EAEC98219")

time.sleep(1)

# 自动登录账户
driver.switch_to_frame('alibaba-login-box')  # 登录框在框架里面
driver.find_element_by_id("fm-login-id").send_keys("kanastal1@163.com")
driver.find_element_by_id("fm-login-password").send_keys("kanastal111")
driver.find_element_by_id("fm-login-submit").click()


