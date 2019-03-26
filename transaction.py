import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
import json
import time

class HuoBispider(object):
    def login(self):
        url = 'https://www.huobi.br.com/-/x/uc/uc/open/risk/control'
        headers = {
            'content-type': 'application/json;charset=UTF-8',
            "Origin": "https://www.huobi.br.com",
            "Referer": "https://www.huobi.br.com/zh-cn/login/?backUrl =/zh-cn/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }
        data = {
            "login_name":"wang.hiqi@gmail.com",
            "scene":2,
            "source":1,
            "fingerprint":"28265f48d4d741fe35a024f0b761c940",
            "version":2
            }
        res = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(res.text)

    # def auth(self):
    #     url = "https://www.huobi.br.com/-/x/uc/uc/open/login"
    #     #滑动验证请求
    #     headers = {
    #         'content-type': 'application/json;charset=UTF-8',
    #         "Origin": "https://www.huobi.br.com",
    #         "Referer": "https://www.huobi.br.com/zh-cn/login/?backUrl =/zh-cn/",
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    #     }
    #     data ={
    #             "way": "WEB",
    #             "password": "38d6600875783b90aa0efec83579519f",
    #             "login_name": "wang.hiqi@gmail.com",
    #             "fingerprint": "28265f48d4d741fe35a024f0b761c940",
    #             "afs": {
    #                 "platform": "3",
    #                 "csessionid": "01kIuB6rE7Sn1ALRuvEaV799fFCbgMmty9WOA0qYy2Vvcbs41j5j3u63scYG61-F9jg2993YvW93EXJIQAmGtRy-WMsIsoEuz0kKp9vrymPCFPwwIWh5-mCKTHbuJ6JjJmmaIku32Mcb1lPo8a5_p71XqTnl8_3WW2Uhg3oJ-7Wkn77k5naJQXLmWrL_uHm89tPW0Zuz_q-I6vPjhrO8pmng",
    #                 "value": "pass",
    #                 "sig": "05a1C7nT4bR5hcbZlAujcdycQZP-iQgHRQJKb-FddL2dxZZixKVwdn16fQR6PXAfBbLRTzh9o-6fH9FRHnZS6fcy1lOqMbLNNA_m3OZyRYUt4Lw697TLYp5DAATbgDnbE-jbT7Imy5dcsDEFZXpwKStQ-r17KOm0pVjxcvG1WKT1shk9F4luekAU0G0W0OIvS4erMp776BlwGNj7FWAXyY72g_XJUVpY7cqCsjmnAVMglaUJU2g-Dpi_XenL-nsYWqCD7RBriG6_I3-IMPUHLq6a2KIp70TV_EQLIhsZgzXEARR_6To6GviC3tIb2jMyFDcxX9k8Li9HStAw8QfUEec207-TaKiwmjpBlHYDmJwzkbPWbnshKPYvqI3Q0qUg0UbaqhPjUjeBIQn7m5FjiHsKeC98oBGuHQ2Qk1k5E2qqJYvyYaHzUZr-jgKU9WIDA4Y3JJ3zep7Mi39OdTKQeacaDFvK44SjQMnjchhR_MoQQ",
    #                 "token": "FFFF0000000001796AA8:1553150259038:0.030983791382810377",
    #                 "scene": "login",
    #                 "session": "01kIuB6rE7Sn1ALRuvEaV799fFCbgMmty9WOA0qYy2Vvcbs41j5j3u63scYG61-F9jg2993YvW93EXJIQAmGtRy-WMsIsoEuz0kKp9vrymPCFPwwIWh5-mCKTHbuJ6JjJmmaIku32Mcb1lPo8a5_p71XqTnl8_3WW2Uhg3oJ-7Wkn77k5naJQXLmWrL_uHm89tPW0Zuz_q-I6vPjhrO8pmng"
    #             }
    #         }
    #     data1 = {
    #         "way": "WEB",
    #         "password": "38d6600875783b90aa0efec83579519f",
    #         "login_name": "wang.hiqi@gmail.com",
    #         "fingerprint": "28265f48d4d741fe35a024f0b761c940",
    #         "afs": {
    #             "platform": "3",
    #             "csessionid": "0117s2gxgxya0KLW-E4W4nPQMjZzsfPQKyUvsaCKDWqGJQeQNmfLTnnIdgdp1unetImE-RV1zyZnKomVg0SD7BDP0gAr0O8tIId3dMSMVprRhgj08S1T5hVVoDayX289iJod8zdTOq9ePwqlbvCh1hI3ksnBz3cdNI797CqvpyvL14IAZzgHeuvfBcungdV2vb4NSZrZlUUo2sM9IA_BjoHQ",
    #             "value": "pass",
    #             "sig": "05a1C7nT4bR5hcbZlAujcdyQbbDUyOGWDwylifefSUPHxZZixKVwdn16fQR6PXAfBbK19hhRZlMJmkJ2gMyPQ3Uw6wISOKuapKF0tXybdOwqB9xL7VSPQ2vGrFCu_Zan3rxPYVGL3Ke_3fpSqjQrNvdjEs-dxLcsPU89IfMt-Z0XlwPwSnW2ocf2cNwOO_J_oxN4DZRKSBKr17Ukdkyfcj3cyt_0vcFoIkamiMUS4vFhuPuqhHIKg-Xq1epdkhFh7mExhygtd82qIZTMnCDt79IWM_mwq8nBukVsj-Eo7Ici9szLjS00-MsIUnK5Hvkh0HJSwlrGLddKOfNJ-i-06wbdhCwadI1LPFGeiZi5h7NY6g8X3pt_4ypuCuh8xhdUTqfOjH0moOB5z3_L-KUxM3px7lj5PMEC7aMIdwlPReGamhCdL-YxBAb7HGcGqyXLOzKtt6DgN1GsLYykoP1XvNergA-hEtcn6DHn-NPKSAirM",
    #             "token": "FFFF0000000001796AA8:1553151619283:0.24895385791688374",
    #             "scene": "login",
    #             "session": "0117s2gxgxya0KLW-E4W4nPQMjZzsfPQKyUvsaCKDWqGJQeQNmfLTnnIdgdp1unetImE-RV1zyZnKomVg0SD7BDP0gAr0O8tIId3dMSMVprRhgj08S1T5hVVoDayX289iJod8zdTOq9ePwqlbvCh1hI3ksnBz3cdNI797CqvpyvL14IAZzgHeuvfBcungdV2vb4NSZrZlUUo2sM9IA_BjoHQ"
    #         }
    #     }
    #     res = requests.post(url=url, data=json.dumps(data), headers=headers)
    #     print(res.text)


if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(options=option)
    browser.get("https://www.huobi.br.com/zh-cn/login/?backUrl=/zh-cn/")

    # browser.find_element_by_name("login_name").send_keys('wang.hiqi@gmail.com')
    # browser.find_element_by_xpath('//*[@name="login_name"]').send_keys('wang.hiqi@gmail.com')
    # browser.find_element_by_name("password").send_keys('111111')
    # while True:
    # browser.find_elements_by_class_name("btn_submit")[0].click()
    # time.sleep(5)

    while True:
        dragger = ''
        try:
            print(1)
            js = 'document.querySelectorAll("div")[13].style.display = "block";'
            browser.execute_script(js)
            dragger = browser.find_element_by_xpath('//div//span[@class="nc_iconfont btn_slide"]')
        except Exception as e:
            print(e)
            pass
        if dragger:
            print(2)
            break
    # dragger = browser.find_element_by_xpath('//div//span[@class="nc_iconfont btn_slide"]')
    action = ActionChains(browser)
    action.click_and_hold(dragger).perform()
    #
    try:
        action.move_by_offset(150, 0).perform()  # 平行移动鼠标
    except UnexpectedAlertPresentException:
        pass
    action.reset_actions()
    time.sleep(0.1)  # 等待停顿时间
    try:
        action.move_by_offset(120, 0).perform()  # 平行移动鼠标
    except UnexpectedAlertPresentException:
        pass
    action.reset_actions()
    time.sleep(0.2)  # 等待停顿时间
    try:
        action.move_by_offset(150, 0).perform()  # 平行移动鼠标
    except UnexpectedAlertPresentException:
        pass
    action.reset_actions()
    # spider = HuoBispider()
    # spider.login()
    # spider.auth()