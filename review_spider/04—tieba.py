from urllib import request,parse
from create_useragent import get_ua,get_filename
import os

def get_html(wd):
    wd = parse.quote(wd)
    url = 'https://tieba.baidu.com/f?kw={}&pn={}'
    headers = {'User-Agent':get_ua()}
    for i in range(3):
        pn = i * 50
        url = url.format(wd,pn)
        req = request.Request(url, headers=headers)
        res = request.urlopen(req)
        html = res.read().decode()
        filename = get_filename()
        path = os.getcwd()+'/get_html/'+filename
        with open(path,'w+',encoding='utf-8') as f:
            f.write(html)
