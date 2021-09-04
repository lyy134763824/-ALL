import requests
from lxml import etree
import time
import random
from create_useragent import get_ua
import os
BASE_DIRECTORY = '/home/tarena/'


class CodeSpider:
    def __init__(self):
        self.url = 'http://code.tarena.com.cn/AIDCode/aid2103/00_xunlianying/'
        self.auth = ('tarenacode','code_2013')
        self.headers = {'User-Agent':get_ua()}

    def get_html(self,url):
        res = requests.get(
            url = url,
            auth=self.auth,
            headers = self.headers,
        )
        # res.encoding = 'utf-8'
        return res

    def get_path(self,url):
        path = BASE_DIRECTORY + '/'.join(url.split('//')[1].split('/')[1:-1]) + '/'
        if not os.path.exists(path):
            os.makedirs(path)
        return path


    def parse_html(self,html,url):
        parse_obj = etree.HTML(html)
        href_list  = parse_obj.xpath('//a/@href')[1:]
        filename_list = parse_obj.xpath('//a/text()')[1:]
        #终止条件，没有数据就不爬取
        if not href_list:
            return
        for i in range(len(href_list)):
            if href_list[i].endswith('/'):
                # 注意这里的URL路由拼接地址
                url_2 = url + href_list[i]
                # print(url_2)
                html2 = self.get_html(url_2).text
                self.parse_html(html2,url_2)
            if  href_list[i].endswith('.zip') or href_list[i].endswith('.rar') or href_list[i].endswith('.tar.gz'):
                # print(url,href_list[i])
                self.save_file(url+href_list[i],filename_list[i])

    def save_file(self,url,name):
        res = self.get_html(url).content
        path =  self.get_path(url)
        filename = path + name
        with open(filename,'wb+') as f:
            f.write(res)


    def run(self):
        html = self.get_html(self.url).text
        self.parse_html(html,self.url)

if __name__ == '__main__':
    s = CodeSpider()
    s.run()