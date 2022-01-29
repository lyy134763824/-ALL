import multiprocessing as mp
import time,os

#直到所有的进程执行完才会销毁
def fun(n):
    time.sleep(2)
    print(f"{n}:执行是",os.getpid())
    return n*n

pool = mp.Pool()
r = pool.map(func=fun,iterable=[1,2,3,4,5,6])

pool.close()
pool.join()
# 得到进程的返回列表
print(r)