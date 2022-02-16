import multiprocessing as mp
import time,os
from threading import Thread,Lock

def count(x,y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1

def io():
    write()
    read()

def write():
    f = open('io.txt','w+')
    for i in range(1800000):
        f.write('hello word \n')
    f.close()

def read():
    f = open('io.txt','r+')
    f.readline()
    f.close()
