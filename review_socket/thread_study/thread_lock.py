'''

lock 不能重复上锁
with lock:
    print('==='自动解锁)
'''
from threading import Event,Thread,Lock
import time
e = Lock()
a = b = 0
def ya_zi_rong():
    while True:
        e.acquire()
        if a != b:
            print('a= %d,b = %d'%(a,b))
        else:
            print('a= %d,b = %d' % (a, b))
        e.release()
t = Thread(target=ya_zi_rong)
t.start()
while True:
    with e:
        a += 1
        b += 1
t.join()

























































