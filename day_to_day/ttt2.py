'''
* Created with Pycharm IDEA.
 * @Project      : lyy_styudy
 * @FileName     : ttt2.py
 * @createTime   : 2021/12/10 19:13
 * @version      : 1.0
 * @author       : Lyy
 * @Email        : 2793008966@qq.com
'''

import requests
from fake_useragent import  UserAgent
proxy ={'HTTP': '139.198.124.115:59394'}
headers= {'User-Agent':str(UserAgent(verify_ssl=False).random)}
html = requests.get('https://www.baidu.com/',proxies=proxy,headers = headers)
# print(html.text)
# print(html.status_code)
# print(html)
a = {'a':1}
b = {'b':1}
a.update(b)
print(a)
