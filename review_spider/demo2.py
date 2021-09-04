import requests
import re
from urllib import parse,request
from create_useragent import  get_ua
import time
import random
import pymysql

# re_bds = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?release="time">(.*?)</p>',re.S)
# res = requests.get('https://maoyan.com/board/4?offset=50')
# print(res.text)

class MaoYan:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.list1 = []
        self.i = 0
        self.db = pymysql.connect(
            '127.0.0.1',
            'lyy',
            '123',
            'maoyan_db',
            charset='utf8',
        )
        self.cursor = self.db.cursor()



    def get_html(self,url):
        headers = {'User-Agent':get_ua()}
        # prox = [
        #     {'http':'114.103.139.240:3256'},
        #     {'http':'120.199.210.18:8383'},
        #     {'http':'112.195.243.71:3256'},
        # ]
        req = request.Request(url=url,headers=headers)
        res = request.urlopen(req)
        # oxy = random.choice(prox)
        # oxy_handle = request.ProxyHandler(oxy)
        # opener = request.build_opener(oxy_handle)
        # res = opener.open(url)
        html = res.read().decode()
        # print(html)
        time.sleep(random.uniform(1,3))
        # print(html)
        return html

    def parse_html(self,html):
        pattern = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>',re.S)
        res = pattern.findall(html)
        dict1 = {}
        for i in res:
            dict1['name'] = i[0].strip()
            dict1['star'] = i[1].strip()
            dict1['time'] = i[2].strip()[5:15]
            self.i += 1
            self.list1.append((dict1['name'], dict1['star'], dict1['time']))




    def write_mysql(self):
        if not self.list1:
            return '空数据'
        ins = 'insert into filmtab values(%s,%s,%s)'
        self.cursor.executemany(ins,self.list1)
        self.db.commit()




    def run(self):
        for i in range(5):
            url = self.url.format(10*i)
            html = self.get_html(url)
            self.parse_html(html)
        # print('一共：', self.i)
        # print(self.list1)
        self.write_mysql()
        self.db.close()
        self.cursor.close()


        
if __name__ == '__main__':
    # a = MaoYan()
    # a.run()
    proxy = {'http':'101.200.127.149:3129'}
    try:
        requests.adapters.DEFAULT_RETRIES=3
        res = requests.get('https://www.baidu.com/',timeout=8,proxies=proxy,headers={'User-Agent': get_ua()})
        print(res.i)
    except:
        print('NO')
    # thisip = ''.join('106.45.105.180:3256'.split(':')[0:1])
    # print(thisip)
    # if res == "http://"+proxy['http']:
    #     print('ok')