import multiprocessing as mp
import time,os




def fun1(sec,name):
    time.sleep(sec)
    print(mp.current_process().name)
    print(f'树胶-{name}',os.getppid(),"---->",os.getpid(),)

p = mp.Process(target=fun1,kwargs={'name':'fun1','sec':2})


p.start()
# 子进程随着父进程推出而推出
# p.daemon = True
print('pid:',p.pid)
print('name:',p.name)
print('is_active:',p.is_alive())
p.join()
print('is_active:',p.is_alive())
