import excel
import function as fc
from selenium import webdriver
import json

# 获取excel数据
data = excel.get_data()

# 设置Chrome浏览器
#options = webdriver.ChromeOptions()
# options.add_argument("--headless")
#driver = webdriver.Chrome(chrome_options=options)

with open("Chrome进程值.txt", "r") as fp:
    load_dict = json.load(fp)

driver = webdriver.Remote(command_executor=load_dict["executor_url"], desired_capabilities={})
driver.session_id = load_dict["session"]


while 1:
    c = input("请输入产品型号:")

    profile = excel.search_by_id(str(c), data)

    if not profile:
        print("找不到该产品")
        continue

    fc.go_post_page(driver, profile)  # 打开产品发布页
