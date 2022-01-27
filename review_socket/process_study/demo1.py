'''
同时差分文件
io行为最好s1 zi jincheng zuo
'''

import multiprocessing as mp
import time,os

filename = 'tt.jpeg'
size = os.path.getsize(filename)
print(size)
def top():
    fr = open(filename,'rb+')
    fw = open('top.jpg','wb+')
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()

def bot():
    fr = open(filename, 'rb+')
    fw = open('bot.jpg', 'wb+')
    n = size // 2
    fr.seek(n,0)
    fw.write(fr.read())
    fr.close()
    fw.close()


p1 =mp.Process(target=top)
p2 =mp.Process(target=bot)
p1.start()
p2.start()
p1.join()
p2.join()