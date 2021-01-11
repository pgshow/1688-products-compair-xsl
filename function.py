import time
import json
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    # 自动登录账户
    driver.get(
        "https://login.aliexpress.com/buyer.htm?spm=a2g1y.promotion-20181111.1000002.7.311f5e28ugMVc2&return=https%3A%2F%2Fwww.aliexpress.com%2Fstore%2F4282057%3Fspm%3D2114.10010108.0.0.433e2daaVKvagh&from=lighthouse&random=C3E91EFF317077B02C559F1EAEC98219"
    )

    time.sleep(1)
    driver.switch_to_frame('alibaba-login-box')  # 登录框在框架里面
    driver.find_element_by_id("fm-login-id").send_keys("kanastal1@163.com")
    driver.find_element_by_id("fm-login-password").send_keys("kanastal111")
    driver.find_element_by_id("fm-login-submit").click()

    # while not driver.find_elements_by_xpath("//a[contains(text(),'卖家后台')]"):
    #     print("等待登陆中……")
    #     time.sleep(1)

    while not driver.get_cookie("_hvn_login"):
        print("等待登陆中……")
        time.sleep(1)

    # 导出cookie
    cookies = driver.get_cookies()
    with open("cookies.txt", "w") as fp:
        json.dump(cookies, fp)


def check_cookie(driver):
    # 检查用户登录情况
    if not driver.get_cookie("_hvn_login"):
        # 导入cookie
        driver.get("https://helppage.aliexpress.com/buyercenter/index.htm")
        try:
            with open("cookies.txt", "r") as fp:
                cookies = json.load(fp)
                for cookie in cookies:
                    # cookie.pop('domain')  # 如果报domain无效的错误
                    driver.add_cookie(cookie)
        except:
            time.sleep(1)
            login(driver)

    time.sleep(1)

    # 导入的cookie如果失效再登录
    if not driver.get_cookie("_hvn_login"):
        login(driver)


def go_post_page(driver, profile):
    # check_cookie(driver)

    print(profile)

    driver.get("http://post.aliexpress.com/offer/post_ae_product.htm?catId=33902")  # 太阳眼镜的发布页

    # 使用 selenium 显示等待

    # 选择品牌
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="property-id-2"]/div/div'))
    element.click()
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="property-id-2"]/div/div/div[2]/ul/li[2]').is_displayed())
    driver.find_element_by_xpath('//*[@id="property-id-2"]/div/div/div[2]/ul/li[2]').click()

    # 适应人群
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="property-id-200000043"]/div/div'))
    element.click()
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="property-id-200000043"]/div/div/div[2]/ul/li[2]').is_displayed())
    driver.find_element_by_xpath('//*[@id="property-id-200000043"]/div/div/div[2]/ul/li[2]').click()

    # 高度
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="property-id-200000285"]/div/input'))
    element.send_keys("mm")

    # 宽度
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="property-id-200000286"]/div/input'))
    element.send_keys("mm")

    # 型号
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="property-id-3"]/div/input'))
    element.send_keys(profile[1])

    # 标题
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="title"]/div/div[2]/input'))
    element.send_keys(profile[3])

    # 零售价
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="sku"]/div/div[3]/div[2]/input'))
    element.send_keys("59")

    # 批发
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="sku"]/div/div[7]/div[2]/div/label'))
    element.click()

    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="sku"]/div/div[7]/div[2]/div[2]/div/input[1]').is_displayed())
    driver.find_element_by_xpath('//*[@id="sku"]/div/div[7]/div[2]/div[2]/div/input[1]').send_keys("10")

    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="sku"]/div/div[7]/div[2]/div[2]/div/input[2]').is_displayed())
    driver.find_element_by_xpath('//*[@id="sku"]/div/div[7]/div[2]/div[2]/div/input[2]').send_keys("10")

    # 包装信息
    element = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath('//*[@id="package-info"]/div/div[1]/div[2]/div[1]/input'))
    element.send_keys("0.1")

    element = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath('//*[@id="package-info"]/div/div[2]/div[2]/input[1]'))
    element.send_keys("18")

    element = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath('//*[@id="package-info"]/div/div[2]/div[2]/input[2]'))
    element.send_keys("10")

    element = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath('//*[@id="package-info"]/div/div[2]/div[2]/input[3]'))
    element.send_keys("8")

    # 产品运费模板
    element = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath('//*[@id="freight-template"]/div/div[2]/div'))
    element.click()

    WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath('//*[@id="freight-template"]/div/div[2]/div[1]/div[2]/ul/li[1]').is_displayed())
    driver.find_element_by_xpath('//*[@id="freight-template"]/div/div[2]/div[1]/div[2]/ul/li[1]').click()

    # 发货期
    element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="delivery-time"]/div/div[2]/input'))
    element.send_keys("7")

    # 产品分组
    element = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath('//*[@id="group"]/div/div[2]/div'))
    element.click()

    WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath('//*[@id="group"]/div/div[2]/div/div[2]/ul/li[1]').is_displayed())
    driver.find_element_by_xpath('//*[@id="group"]/div/div[2]/div/div[2]/ul/li[1]').click()

    # 产品有效期
    element = WebDriverWait(driver, 10).until(
        lambda x: x.find_element_by_xpath('//*[@id="other"]/div[2]/div[1]/div[2]/div/label[1]'))
    element.click()

    print("表单填写完毕")

