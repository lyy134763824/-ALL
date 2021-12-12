


import re
str1 = "https://search.jd.com/Search?keyword=%E5%85%AB%E7%88%AA%E7%83%A7%E4%BA%AC%E4%B8%9C%E8%87%AA%E8%90%A5&qrst=1&suggest=1.def.0.base&wq=%E5%85%AB%E7%88%AA%E7%83%A7%E4%BA%AC%E4%B8%9C%E8%87%AA%E8%90%A5&stock=1&pvid=8a940fce999243b3921ea01bd83f1d66&psort=3&click=0"
# keyword=&qrst=1&suggest=1.def.0.base&wq=&stock=1&psort=3&click=0

def get_dict(tar):
    rs_list = tar.split('?')[1].strip().split('&')
    # print(rs_list)
    item = {}
    count = 0
    tmp = []
    for i in rs_list:
        print(i.split('='))
        item[i.split('=')[0]] = i.split('=')[1]
    #     if "%" in i.split('=')[1] or len(i.split('=')[1]) > 10:
    #         count += 1
    #         tmp.append(i)
    #     else:
    #         item[i.split('=')[0]]  = i.split('=')[1]
    # print(f'过滤了{count}个分别是{tmp}')
    return item
print(get_dict(str1))