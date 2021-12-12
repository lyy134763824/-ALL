from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
from day_to_day.find_snaks import *
from fake_useragent import UserAgent
'''
# J = JudGe()
# print(J.run('https://item.jd.com/859557.html'))
# J.run('https://item.jd.com/69942152195.html')
食品饮料>休闲食品>休闲零食>零食大礼包>良品铺子 >良品铺子 猪事顺利巨型零食大礼包猪饲料礼包 零食大礼包送女友25包零食生日礼物送女友节日送礼团购 【14款荤素分享包】小时刻零食大礼包1426g x1袋良品铺子官方旗舰店联系客服关注店铺

食品饮料>休闲食品>休闲零食>果冻/布丁>喜之郎 >喜之郎果冻自营喜之郎京东自营旗舰店关注店铺
'''


# 想要校验的列
LIANJ = 'C'
# 食品名字存在的列
NAME = 'B'
FiLe_name = 'xxx.xlsx'

class JudGe:
    #京东链接的提取xpath
    Test = 3
    XPATH = '//div[@id="crumb-wrap"]'
    def __init__(self):
        self.headers = {'User-Agent':str(UserAgent(verify_ssl=False).random)}
        # options = Options()
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options)
        # self.driver = webdriver.Chrome()
        self.timeout = WebDriverWait(driver=self.driver,timeout=10)
        self.count = 0

    def get_html(self,addr):
        self.driver.get(addr)
        try:
            self.timeout.until(EC.presence_of_element_located((By.ID,"crumb-wrap")))
        except:
            self.count += 1
            if self.count <= JudGe.Test:
                #刷新再试试
                self.driver.refresh()
                return self.get_html(addr)
            else:
                return f'超过最大尝试次数，链接是{addr}'
        innerText = self.driver.find_element_by_xpath(JudGe.XPATH).get_attribute('innerText')
        # innerText = self.driver.find_element_by_xpath(JudGe.XPATH).get_attribute('textContent')
        res = innerText.strip().replace('\n','')
        return res



    def run(self,addr):
        content = self.get_html(addr)
        if not content:
            return False
        elif   '自营' in content :
            return True
        else:
            return False


class Auto:
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
                    print(f"行数是{i+1}：{sheet1[NAME][i].value} 的链接是: {sheet1[LIANJ][i].value} 为非自营店")
                    item[sheet1[NAME][i].value] = sheet1[LIANJ][i].value
        return item



if __name__ == '__main__':
    A = Auto()
    f = F_s()
    item = A.run()
    for key in item.keys():
        f.run(key)

