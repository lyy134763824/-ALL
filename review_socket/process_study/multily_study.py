import multiprocessing as mp
import time,os
'''
进程与进程之间1是独立的空间
start开始进程
之间的是父进程空间
join 父进程回收

'''
def fun1(sec,name):
    time.sleep(sec)
    print(f'树胶-{name}',os.getppid(),"---->",os.getpid(),)

def fun2(sec,name):
    time.sleep(sec)
    print(f'吃饭-{name}',os.getppid(),"---->",os.getpid(),)
def fun3(sec,name):
    time.sleep(sec)
    print(f'大豆都-{name}',os.getppid(),"---->",os.getpid(),)
st = [fun1,fun2,fun3]
jobs = []

for i in range(len(st)):
    # p = mp.Process(target=st[i],args=(i,f"fun{i+1}"))
    p = mp.Process(target=st[i],kwargs={'name':f'fun{i+1}','sec':i+1})
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()