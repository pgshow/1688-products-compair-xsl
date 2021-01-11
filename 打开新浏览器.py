import json
from selenium import webdriver


# 设置Chrome浏览器
options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument("--start-maximized")
options._arguments = ['disable-infobars']

# 对应你的chrome的用户数据存放路径,带入 chrome已经有的cookie
# options.add_argument(r"user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Default")
options.add_argument('--proxy-server=http://127.0.0.1:8080')  # 使用mitmdump避免被检测

driver = webdriver.Chrome(chrome_options=options)

# 获取webdriver远程ID,第一个是会话的sessionId,第二个就是命令执行器连接
executor_url = driver.command_executor._url
session_id = driver.session_id

# 保存浏览器进程值
with open('Chrome进程值.txt', 'w') as json_file:
    json.dump({"session": session_id, "executor_url": executor_url}, json_file, ensure_ascii=False)

print("请登录速卖通！")


# # 导入cookie
driver.get("https://www.aliexpress.com/")
# with open("cookies.txt", "r") as fp:
#     cookies = json.load(fp)
#     for cookie in cookies:
#         # cookie.pop('domain')  # 如果报domain无效的错误
#         driver.add_cookie(cookie)
