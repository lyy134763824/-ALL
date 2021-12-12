import time

import pymysql
import requests
from openpyxl import load_workbook
from lxml import etree
from day_to_day.find_snaks import *
from fake_useragent import UserAgent
import re


# 想要校验的列
LIANJ = 'M'
# 食品名字存在的列
NAME = 'L'
FiLe_name = 'xxx.xlsx'

#切换代理






class JudGe:
    #京东链接的提取xpath
    XPATH = '//div[@id="crumb-wrap"]//em'
    def __init__(self):
        self.headers = {'User-Agent':str(UserAgent(verify_ssl=False).random),}
        # self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'}
        self.db = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='123456',
            database='proxy_db',
            charset='utf8',
        )
        self.cursor = self.db.cursor()

    def judge_proxy(self):
        pass
        proxies = {'https': '101.236.54.97:8866'}



    def get_html(self,addr):
        html = requests.get(addr,headers=self.headers)
        if "window.location.href" in html.text and len(html.text) < 100:
            temp = html.text
            pattern = r"href='(.*?)'<"
            addr2 = re.findall(pattern=pattern,string=temp)[0]
            # print(addr2)
            time.sleep(2)
            self.get_html(addr2)
        else:
            # print(html.text)
            time.sleep(5)
            return html.text

    def parse_html(self,addr):
        html = self.get_html(addr)
        # print('*'*50)
        # print(html)
        htmlElement  = etree.HTML(html)

        text =htmlElement.xpath(JudGe.XPATH)
        if not text:
            return None
        text = text[0].text.strip()
        return text

    def run(self,addr):
        content = self.parse_html(addr)
        if not content:
            return False
        elif   '自营' in content :
            return True
        else:
            return False


class aoto:

    def __init__(self):
        self.j = JudGe()

    def run(self):
        wb = load_workbook(FiLe_name)
        sheets = wb.worksheets
        sheet1 = sheets[0]
        #索引下表从0 开始计算8行到10行 3 行  不取10
        n = len(sheet1[LIANJ])
        item = {}
        for i in range(n):
            if sheet1[LIANJ][i].value == None:
                continue
            if "https" in sheet1[LIANJ][i].value:
                if self.j.run(sheet1[LIANJ][i].value):
                    pass
                else:
                    print(f"行数是{i+1}{sheet1[NAME][i].value} 的链接是: {sheet1[LIANJ][i].value} 为非自营店")
                    item[sheet1[NAME][i].value] = sheet1[LIANJ][i].value
        return item
# https://search.jd.com/Search?keyword=%E5%85%AB%E7%88%AA%E7%83%A7%E4%BA%AC%E4%B8%9C%E8%87%AA%E8%90%A5&wq=%E5%85%AB%E7%88%AA%E7%83%A7%E4%BA%AC%E4%B8%9C%E8%87%AA%E8%90%A5&stock=1&psort=3&click=1
# https://search.jd.com/Search?keyword=&wq=%E5%85%AB%E7%88%AA%E7%83%A7%E4%BA%AC%E4%B8%9C%E8%87%AA%E8%90%A5&stock=1&psort=3&click=1
if __name__ == '__main__':
    A = aoto()
    f = F_s()
    item = A.run()
    for key in item.keys():
        f.run(key)



