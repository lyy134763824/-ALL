import os
from urllib import request,parse
from  fake_useragent import UserAgent
# ua = UserAgent(use_cache_server=False,verify_ssl=False,cache=False)
from create_useragent import get_ua
import random
import time
# # url = 'https://www.baidu.com/s?'
url = 'https://www.baidu.com/s?{}'
params = {'wd':'照例因',
          'pn':10}
result = parse.urlencode(params)
headers = {'User-Agent':get_ua()}
# req = request.Request(url+result,headers=headers)
req = request.Request(url.format(result),headers=headers)
res = request.urlopen(req)
print(res.read().decode('UTF-8'))
# print(res.read().decode())


def get_url(word):
    base_url = 'https://www.baidu.com/s?'
    parmas = parse.urlencode({'wd':word})
    return base_url+parmas

# def get_path():
#     num = str(random.randint(0,1000))
#     filename = num+'.html'
#     if not os.path.exists(filename):
#         return filename
#     return get_path

def _get_filename():
    num = str(random.randint(0,60))
    head  =  str(time.strftime('%Y-%m-%d %H:%M:%S'))
    filename = head+' '+num+'.html'
    if not os.path.exists(filename):
        return filename
    return _get_filename

def save_loc(url):
    headers = {'User-Agent':get_ua()}
    req = request.Request(url=url,headers=headers)
    res = request.urlopen(req)
    res = res.read().decode('utf-8')
    filename = _get_filename()
    # path = os.getcwd() + '/get_html'
    # if not os.path.exists(path):
    #     os.mkdir(path)
    # with open(path+'/'+filename,'w+') as f:
    with open(filename,'w+') as f:
        f.write(res)
    f.close()

if __name__ == '__main__':
    url = get_url('niuniu冲')
    save_loc(url)
