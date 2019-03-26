from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(options=option)
browser.get("https://www.huobi.br.com/zh-cn/login/?backUrl=/zh-cn/")
while True:
    s_time = time.strptime('2019-3-23 21:52:00', '%Y-%m-%d %H:%M:%S')
    n_time = time.time()
    if n_time >= time.mktime(s_time):
        browser.find_element_by_xpath("submit bg-buy 0").click()
        print('时间到')
        break


