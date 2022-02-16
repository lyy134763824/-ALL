from threading import Thread

import time
import os
'''
t.is_active()
t.name
t.setName()
t.getName()
t.setDaemon(true)
t.isDaemon()


'''
def music(sec,name):
    time.sleep(sec)
    print(f'爆发那个{name}')
l = ['n','m','o']
jobs = []
for i in range(len(l)):
    t = Thread(target=music,args=(i,l[i]))
    jobs.append(t)
    t.start()
for t in jobs:
    t.join()