import threading
import time
from time import  sleep
import os
a = 1
def fun(l):
    print('start')
    time.sleep(l)
    global a
    print("a=",a)
    a= 1000
    print('end',os.getpid())

t  = threading.Thread(target=fun,args=(3,))
t.start()

sleep(2)
print('main',os.getpid())
t.join()

print('a=',a)