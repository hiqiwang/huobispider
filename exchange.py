import requests
from selenium import webdriver
import json
from multiprocessing import Pool
import configparser
import time


def exchange(token,cookies1,i,cf):
    url = "https://www.huobi.br.com/-/x/pro/v1/order/orders/place"
    headers = {
        'content-type': 'application/json;charset=UTF-8',
        "Origin": "https://www.huobi.br.com",
        "Referer": "https://www.huobi.br.com/zh-cn/exchange/?s=ht_usdt",
        'HB-PRO-TOKEN':token,
        'Connection': 'close',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    data = {
        "stop-price": "",
        "operator": "gte",
        "amount": cf.get("exchange", "amount"),
        "account-id": cf.get("exchange", "account-id"),
        "source": "web",
        "type": "buy-market",
        "symbol": cf.get("exchange", "symbol")
    }
    try:
        print('发起交易请求%d' % i)
        res = requests.post(url=url, data=json.dumps(data), headers=headers,cookies=cookies1)
        print(str(i)+res.text)
    except Exception as e:
        print('下单异常%d:%s' % (i,e))

if __name__ == "__main__":
    cf = configparser.ConfigParser()
    cf.read("config.ini",encoding='UTF-8')

    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(options=option)
    browser.get("https://www.huobi.br.com/zh-cn/login/?backUrl=/zh-cn/")
    while True:
        # s_time = time.strptime(cf.get("exchange", "s_time"), '%Y-%m-%d %H:%M:%S')
        # n_time = time.time()
        # if n_time >= time.mktime(s_time):
        #     print('时间到')
        #     break
        a = input("输入go继续:")
        if a == 'go':
            break
    pool = Pool(processes = 8)
    for i in range(20):
        cookies = browser.get_cookies()
        cookies1 = {}
        for cookie in cookies:
            cookies1[cookie['name']] = cookie['value']
        token = cookies1['HB-PRO-TOKEN']
        robj = pool.apply_async(exchange,(token,cookies1,i,cf,))
    pool.close()
    pool.join()