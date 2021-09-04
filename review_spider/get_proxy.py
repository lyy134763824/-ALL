'''
https://www.kuaidaili.com/free/
爬取可用的代理IP

4172頁的代理ip
'''
from  lxml import etree
import requests
from create_useragent import get_ua
import time
import random
import pymysql
#代理地址西刺代理，快代理，全网代理，代理精灵
#測試代理IP可用的IP地址  http://ip.yqie.com/proxyhttps/
# TEST_URL = 'http://icanhazip.com/'
TEST_URL = 'https://www.baidu.com/'

class SpiderProxy(object):
    def  __init__(self):
        self.url = 'https://www.kuaidaili.com/free/inha/{}/'
        self.headers = {'User-Agent': get_ua()}
        self.db = pymysql.connect(
            '127.0.0.1',
            'lyy',
            '123',
            'proxy_db'
        )
        self.cursor = self.db.cursor()
        self.list_ip = []


    def get_html(self,url):
        res = requests.get(url=url,headers=self.headers)
        res.encoding='utf-8'
        return res.text

    def parse_html(self,url):
        html = self.get_html(url)
        parse_obj = etree.HTML(html)
        tr_list = parse_obj.xpath('//*[@id="list"]/table/tbody/tr')
        for tr in tr_list:
            item = {}
            ip_xpath = './td[@data-title="IP"]/text()'
            ip = tr.xpath(ip_xpath)
            item['IP'] = [ip[0].strip() if ip else None][0]
            item['PORT'] = tr.xpath('./td[@data-title="PORT"]/text()')[0]
            item['匿名度'] = tr.xpath('./td[@data-title="匿名度"]/text()')[0]
            item['类型'] = tr.xpath('./td[@data-title="类型"]/text()')[0]
            item['位置'] = tr.xpath('./td[@data-title="位置"]/text()')[0]
            item['响应速度'] = tr.xpath('./td[@data-title="响应速度"]/text()')[0]
            # {'IP': '117.64.237.23', 'PORT': '1133', '匿名度': '高匿名', '类型': 'HTTP', '位置': '安徽省合肥市  电信', '响应速度': '0.6秒'}
            # print(item)
            flag = self.judge_ip(item['类型'],item['IP'],item['PORT'])
            print('flag',flag)
            if flag:
                flag2 = self.judge_sql(item)
                print('flag2',flag2)
                if flag2:
                    self.list_ip.append((item['IP'], item['PORT'], item['匿名度'],item['类型'],item['位置'],item['响应速度'], time.strftime('%Y-%m-%d %H:%M:%S')))

    def judge_ip(self,hp,ip,pt):
        proxy = { hp: ip+":"+pt }
        try:
            #设置最大的重连次数
            requests.adapters.DEFAULT_RETRIES = 2
            res = requests.get(TEST_URL,proxies=proxy,timeout=5,headers=self.headers)
            if res.status_code == 200 :
                return True
        except:
            print('這個不行:', proxy)
            return None


    def judge_sql(self,item):
        ins_selct = 'select IP,PORT,TYPE from proxy_ip where IP = %s and PORT = %s and TYPE = %s'
        self.cursor.execute(ins_selct,(item['IP'], item['PORT'], item['类型']))
        data = self.cursor.fetchall()
        print('data',data)
        if not data:
            return True
        else:
            print('已经存在')


    def save_ip(self):
        ins = 'insert into proxy_ip values(%s,%s,%s,%s,%s,%s,%s)'
        try:
            self.cursor.executemany(ins,self.list_ip)
            self.db.commit()
        except Exception as e:
            print(e)
            self.db.rollback()


    def run(self,start,end):
        for i in range(start,end+1):
            url = self.url.format(i)
            self.parse_html(url)
            time.sleep(random.uniform(2,3))
        print(self.list_ip)
        self.save_ip()
        self.db.close()
        self.cursor.close()

if __name__ == '__main__':
    g = SpiderProxy()
    g.run(1,5)








