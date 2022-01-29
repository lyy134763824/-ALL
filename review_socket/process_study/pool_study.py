import multiprocessing as mp
import time,os

def fun(msg):
    time.sleep(2)
    print(f"{msg}:信息是",os.getpid())
    return msg
# 2 代表两个进程并用
pool = mp.Pool(15)
start = time.time()
for i in range(10):
    msg = f"this is {i}"
    # 添加到等待队列中就已经开始执行了 异步同时执行
    # s = pool.apply_async(func=fun,args=(msg,))
    # 同步执行  即 一步一步来  必须上一步完成才能完成后面的步骤
    s = pool.apply_async(func=fun,args=(msg,))
    # 获取fun函数的返回值
    print(s.get())
# 后面父进程`结束  子进程也会随之结束


#关闭进程池
pool.close()
#回收进程池
pool.join()
print("运行时间%.2f"%(time.time() - start))














