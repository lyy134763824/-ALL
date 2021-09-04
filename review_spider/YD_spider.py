
import time
import random
import requests
from hashlib import md5
import json
import pymysql

class YD_spider:
    def __init__(self):
        self.url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh,zh-CN;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,or;q=0.5',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '238',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-2115479730@117.154.102.33; JSESSIONID=aaa6k59n0DQo8-8FCdXUx; OUTFOX_SEARCH_USER_ID_NCOO=428397696.72336763; fanyi-ad-id=115021; fanyi-ad-closed=0; SESSION_FROM_COOKIE=ChaZD-backup-2; ___rl__test__cookies=1630763237800',
            'Host': 'fanyi.youdao.com',
            'Origin': 'https://fanyi.youdao.com',
            'Pragma': 'no-cache',
            'Referer': 'https://fanyi.youdao.com/',
            # 'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            # 'sec-ch-ua-mobile': '?0',
            # 'Sec-Fetch-Dest': 'empty',
            # 'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        self.db = pymysql.connect(
            host='127.0.0.1',
            user='lyy',
            password='123',
            database='proxy_db',
        )
        self.cursor = self.db.cursor()


    def get_proxy(self):
        ins = 'select * from proxy_ip order by create_time desc limit 10'
        try:
            self.cursor.execute(ins)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()
        temp = self.cursor.fetchall()
        # ('112.195.240.246', '3256', '高匿名', 'HTTP', '中国 四川 眉山 联通', '0.3秒', '2021-08-22 15:37:14', 9)

        temp2 = random.choice(temp)
        proxy = {temp2[3]:temp2[0]+":"+temp2[1]}
        print(proxy)
        return proxy

    def get_ts_sign_salt(self,word):
        #ts
        ts = str(int(time.time()*1000))
        # salt
        salt = ts + str(random.randint(0,9))
        #sign
        string = "fanyideskweb" + word + salt + "Y2FYu%TNSbMCxc3t2u^XT"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()
        return ts,sign,salt

    def get_post(self,word):
        proxy = self.get_proxy()
        proxy = proxy  if  proxy else {}
        data = self.get_data(word)
        res = requests.post(url=self.url,data=data,headers=self.headers,proxies=proxy)
        return res.text

    def get_data(self,word):
        tp = self.get_ts_sign_salt(word)
        data = {
            'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': tp[2],
            'sign': tp[1],
            'lts': tp[0],
            'bv': '89e18957825871c419be045180c67d3b',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        return data


    def run(self):
        word  = input('请输入查询的单词：')
        res = self.get_post(word)
        res2 = json.loads(res)
        res3 = res2['translateResult'][0][0]['tgt']
        print(f'结果是：{res3}')

if __name__ == '__main__':
    yd = YD_spider()
    yd.run()
