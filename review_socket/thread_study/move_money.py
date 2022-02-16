
from threading import Event,Thread,Lock
import time
class Account:
    def __init__(self, id, balance, lock):
        self.id = id
        self.blance = balance
        self.lock = lock
    def add_my(self,money):
        self.blance += money

    def deposit_my(self,money):
        self.blance -= money

    def get_balance(self):
        return self.blance


a = Account('alex',10000,Lock())
b = Account('bbq',20000,Lock())

def tanserform(give,recv,money):
    if give.lock.acquire():
        give.deposit_my(money)
        time.sleep(0.1)
        give.lock.release()
        if recv.lock.acquire():
            recv.add_my(money)
            recv.lock.release()

    print(f'{give.id}给{recv.id}转了{money}钱')
    print(f'{give.id}还有{give.get_balance()}钱')
    print(f'{recv.id}还有{recv.get_balance()}钱')


if __name__ == '__main__':
    t1 = Thread(target=tanserform,args=(a,b,7000))
    t2 = Thread(target=tanserform,args=(b,a,10000))
    t1.start()
    t2.start()
    t1.join()
    t2.join()