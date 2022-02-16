
'''
同一个文件存在多个位置下载

'''
import os
from threading import Event,Thread,Lock
lock = Lock()
urls = [
    '/home/tarena/测试/study_test/',
    '/home/tarena/测试/',
    '/home/tarena/测试/review_socket/',
]
explore = []
# 文本文件.txt
filename = input('请输入文件名:')
filename = '文本文件.txt'
for i in urls:
    if os.path.exists(i+filename):
        explore.append(i+filename)
path_num = len(explore)
file_size = os.path.getsize(explore[0])
block_size = file_size // path_num

fd = open(filename,'wb+')
def load_file(filename,num):
    f = open(filename,'rb')
    sek = block_size * num
    f.seek(sek)
    data = f.read(block_size)
    with lock:
        fd.seek(sek)
        fd.write(data)

num = 0
jobs = []
for path  in explore:
    t = Thread(target=load_file,args=(path,num))
    jobs.append(t)
    t.start()
    num += 1

for i in jobs:
    i.join()