import random
import time
from lxml import etree
import requests
from create_useragent import get_ua

class MINZHEN_Spider:
    def __init__(self):
        self.url = 'http://www.mca.gov.cn/article/sj/xzqh/1980/'


    def get_html(self,url):
        html = requests.get(url=url,headers = get_ua()).text
        par_html = etree.HTML(html)
        #
        list_a = par_html.xpath("//a[@class='artitlelist']")
        for a in list_a:
            name = a.xpath('./@title')[0]
            if name.endswith('行政区划代码'):
                two_url =  'http://www.mca.gov.cn'+a.xpath('./@href')[0]
                print(two_url)
                return two_url


    def get_real_html(self,url):
        # //a[@class='artitlelist']/text()
        # //a[@class='artitlelist']/@href
        html = requests.get(url=url,headers=get_ua()).text
        parse_html = etree.HTML(html)
        two_a = parse_html.xpath('//a[@title=""]')
        for a in two_a:
            if '代码' in a.xpath('./text()')[0]:
                real_html = a.xpath('./@href')[0]
                print(real_html)
                return real_html
    def get_data(self,url):
        html = requests.get(url=url,headers=get_ua()).text
        parse_html = etree.HTML(html)
        tr_list = parse_html.xpath('//tr[@height = "19"]')
        for tr in tr_list:
            code = tr.xpath('./td[2]/text()')[0]
            name = tr.xpath('./td[3]/text()')[0]
            time.sleep(0.05)
            print(code,name)
2

    def run(self):
        url = self.get_html(self.url)
        url2 = self.get_real_html(url)
        self.get_data(url2)

if __name__ == '__main__':
    M = MINZHEN_Spider()
    M.run()
