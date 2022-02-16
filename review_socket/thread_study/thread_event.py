'''

event
'''
from threading import Event,Thread
import time
e = Event()
s = None
def ya_zi_rong():
    print('白汕头')
    global s
    s = 'kkk'
    e.set()

t = Thread(target=ya_zi_rong)
t.start()

s = 'bbb'
# time.sleep(1)

print('duikoul')
e.wait()
if s == 'kkk':
    print('ok',s)
else:
    print('No',s)
t.join()

























































