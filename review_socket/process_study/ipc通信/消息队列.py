import multiprocessing as mp
import time,os

'''
q.full() 判断队列是否满
q.empty() 判断队列是否为空
q.qsize()   判断当前队列有多少消息
q.close()  关闭队列
q.put(data,[block,timeout])
q.get([block,timeout])

'''
# 最多三个消息
# 必须是父进程中创建
q = mp.Queue(3)

def bar():
    for i in range(5):
        q.put(f'hhrr{i}')

def foot():
    while True:
        try:
            print(q.get(timeout=3))
        except Exception as e:
            print(e)
            return
p1 = mp.Process(target= bar)
p2 = mp.Process(target= foot)

p1.start()
p2.start()
p1.join()
p2.join()