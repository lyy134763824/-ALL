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
    for i in range(3):
        time.sleep(sec)
        print(f'爆发那个{name}')
l = ['n','m','o']
jobs = []
for i in range(len(l)):
    t = Thread(target=music,args=(i,l[i]),name=f'test-{i}')
    jobs.append(t)
    # t.setDaemon(True)
    t.start()
    # t.setName(f'ggg-{i}')


for t in range(len(jobs)):
    print(f'name-{t}',jobs[t].getName())
