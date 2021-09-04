from urllib import request,parse
from create_useragent import get_ua,get_filename
import os
import time
import random
class TieBa:
    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?kw={}&pn={}'
        self.headers = {'User-Agent':get_ua()}

    def get_html(self,url,ed='utf-8'):
        req = request.Request(url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode(ed,errors='ignore')
        return html


    def parse_html(self):
        pass

    def save_html(self,html,ed='utf-8',num=0):
        filename = get_filename(num)
        path = os.getcwd() + '/get_html/' + filename
        with open(path, 'w+', encoding=ed) as f:
            f.write(html)

    def run(self,wd,start,end):
        for i in range(start,end+1):
            pn = i * 50
            wd = parse.quote(wd)
            url = self.url.format(wd,pn)
            html = self.get_html(url)
            self.save_html(html,num=i)
            time.sleep(random.randint(1,3))


if __name__ == '__main__':
    t = TieBa()
    wd = input('贴吧名字:')
    start = int(input('起始页:'))
    end = int(input('终止页:'))
    t.run(wd,start,end)
