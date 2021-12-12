'''
* Created with Pycharm IDEA.
 * @Project      : lyy_styudy
 * @FileName     : ttttt.py
 * @createTime   : 2021/12/10 17:28
 * @version      : 1.0
 * @author       : Lyy
 * @Email        : 2793008966@qq.com
'''
from fake_useragent import UserAgent
import re

from lxml import etree
import pymysql
import requests
import time
# str1 = "<script>window.location.href='http://item.jd.com/html/token.html?returnUrl=http%3A%2F%2Fitem.jd.com%2F5759121.html'</script>"
# pattern = r"href='(.*?)'<"
#
# print(re.findall(pattern,str1)[0])

class JudGe:
    #京东链接的提取xpath
    XPATH = '//div[@id="crumb-wrap"]//em'
    TEST_URL = 'https://www.baidu.com/'
    MAX_TEST = 10
    def __init__(self):
        self.headers = {'User-Agent':str(UserAgent(verify_ssl=False).random)}
        # self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'}
        self.db = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='123456',
            database='proxy_db',
            charset='utf8',
        )
        self.cursor = self.db.cursor()
        self.count =0

    def use_proxy(self):
        ins = 'select * from proxy_ip order by rand() limit 1;'
        self.cursor.execute(ins)
        data = self.cursor.fetchall()
        proxies = {data[0][3]:data[0][0]+":"+data[0][1]}
        res = requests.get(JudGe.TEST_URL, proxies=proxies, timeout=5, headers=self.headers)
        if res.status_code == 200 :
           return proxies
        else:
            proxies = self.use_proxy()
            return proxies


    def get_html2(self, addr):
        if self.count > JudGe.MAX_TEST:
            return None
        proxies = self.use_proxy()
        print(proxies)
        html = requests.get(addr, headers=self.headers,proxies=proxies)
        if "验证页" in html.text:
            self.count += 1
            self.get_html2(addr)
        return html.text

    def get_html(self,addr):
        self.headers.update({'Referer':str(addr)})
        html = requests.get(addr,headers=self.headers)
        if "window.location.href" in html.text and len(html.text) < 200:
            '''
            进入此地，说明需要介入代理ip
            '''
            temp = html.text
            pattern = r"href='(.*?)'<"
            addr2 = re.findall(pattern=pattern,string=temp)[0]
            # print(addr2)
            time.sleep(2)
            tt = self.get_html2(addr2)
            print(tt)
            return tt
        else:
            # print(html.text)
            time.sleep(2)
            return html.text

    def parse_html(self,addr):
        html = self.get_html(addr)
        if not html:
            return None
        htmlElement  = etree.HTML(html)

        text =htmlElement.xpath(JudGe.XPATH)
        if not text:
            return None
        text = text[0].text.strip()
        return text

    def run(self,addr):
        content = self.parse_html(addr)
        if not content:
            return "验证页过不去"
        elif   '自营' in content :
            return True
        else:
            return False
J = JudGe()
print(J.run('https://item.jd.com/859557.html'))