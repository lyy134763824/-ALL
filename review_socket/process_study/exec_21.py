
from exec_2 import  *
import multiprocessing as mp
import time,os
from threading import Thread,Lock

#但进程
start = time.time()
# for i in range(10):
    # count(1,1)  # 11.693455219268799
    # io()  # time 11.165588140487671


#进程
jobs = []
# for i in range(10):
#     # p = mp.Process(target=count,args=(0,0)) #  time 5.658598899841309  7.362057685852051
#     p = mp.Process(target=io)   # time 8.067980289459229  8.12425446510315
#     jobs.append(p)
#     p.start()
# for i in jobs:
#     i.join()

#线程
for i in range(10):
    # p = Thread(target=count,args=(0,0))  #time 10.270842790603638
    p = Thread(target=io)  #time time 17.358702659606934
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()


print('time',time.time()-start)
