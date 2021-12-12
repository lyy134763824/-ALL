

import requests
import sys
import time
sys.path.append(__file__)
from lxml import etree

ADDR = 'https://search.jd.com/Search'

class F_s:
    XPATH = '//div[@id="crumb-wrap"]//em'
    # XPATH = '//*[@id="su"]'
    def __init__(self):
        self.headers = {
    'user-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
}

    def get_html(self,addr,params=None):
        html = requests.get(addr,headers=self.headers,params=params)
        time.sleep(0.1)
        # print(html.text)
        return html.text

    def parse_html(self,addr,word):
        word1 = word + "京东自营"
        #'psort': '3' 'click': '0' 代表销量最高
        data = {'keyword': word1, 'psort': '3', 'click': '0'}
        html = self.get_html(addr,params=data)
        htmlElement  = etree.HTML(html)
        li_list = htmlElement.xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_list:
            ll_list = [i for i in li.xpath('.//text()') if i.strip() !='']
            if '自营' in ll_list:
                # print('存在')
                # print(ll_list)
                url = "https:"+li.xpath('.//div[@class="p-name p-name-type-2"]/a/@href')[0]
                name = li.xpath('.//div[@class="p-name p-name-type-2"]/a/@title')[0]
                print(f'原先  {word}  链接有问题，重新找到的：{name,url}')
                return (name,url)
        print('*'*10)
        print(f'{word}  不好找，手动找找呗，别懒')

    def run(self,WD):
        self.parse_html(ADDR,WD)



# https://search.jd.com/Search?keyword=&qrst=1&suggest=1.def.0.base&wq=&stock=1&psort=3&click=0

# https://search.jd.com/Search?keyword=%E5%85%AB%E7%88%AA%E7%83%A7%E4%BA%AC%E4%B8%9C%E8%87%AA%E8%90%A5&psort=3&click=0
# if __name__ == '__main__':
#     f = F_s()
#     f.run('百草味鱿鱼丝京东自营')