
import multiprocessing as mp
import time,os


def get_time(res):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        f = res(*args,**kwargs)
        proce_time = time.time() - start_time
        print(f'proce_{proce_time}')
        return f
    return wrapper

def if_z(n):
    '''

    :param n: 判断是否为质数
    :return:
    '''
    if n<=1 :
        return False
    for i in range(2,int(n)):
        if n % i == 0:
            return False
    return True

@get_time
def no_multiply():
    list_tmp = []
    for i in range(1,100001,):
        if if_z(i):
            list_tmp.append(i)
    sum(list_tmp)

class Pser_multiply(mp.Process):
    def __init__(self,permse,begin,end):
        self.permse = permse
        self.begin= begin
        self.end = end
        super().__init__()
    def run(self):
        for i in range(self.begin, self.end):
            if if_z(i):
                self.permse.append(i)
        sum(self.permse)

@get_time
def use_4_multiply():
    list_tmp = []
    process = []
    # 100001 // 25000 == 4个进程
    for i in range(1,100001,25000):
        p = Pser_multiply(list_tmp,i,i+25000)
        process.append(p)
        p.start()
    [i.join() for  i in process]
@get_time
def use_10_multiply():
    list_tmp = []
    process = []
    # 100001 // 10000 == 10个进程
    for i in range(1,100001,10000):
        p = Pser_multiply(list_tmp,i,i+10000)
        process.append(p)
        p.start()
    [i.join() for  i in process]


if __name__ == '__main__':
    # no_multiply()  # 46秒
    use_4_multiply() # 24秒
    # use_10_multiply()  # 26秒
