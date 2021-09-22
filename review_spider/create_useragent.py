# 方式1: 构建User-Agent池
from random import randint
import random
import time
import os
def get_ua():
    ua_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    ]
    # return ua_list[randint(0,5)]
    return {'User-Agent':random.choice(ua_list)}


def get_filename(num=0):
    if num ==0 :
        num = str(random.randint(0,60))
    head  =  str(time.strftime('%Y-%m-%d %H:%M:%S'))
    filename = head+' '+str(num)+'.html'
    if not os.path.exists(filename):
        return filename

    return get_filename(num)

# print(get_ua())

# 方法2: fake-useragent
# from fake_useragent import UserAgent

# 提示:用此模块构建请求User-Agent先运行(第1次出现异常正常)
# ua = UserAgent()
# print(ua.random)


