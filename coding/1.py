#!/usr/bin/python

import multiprocessing
import time

def printNum(num):
    time.sleep(num)
    print(num)

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=printNum,args=(i,))
        p.start()

    print('CPU number:',multiprocessing.cpu_count())
    print('total active process:',len(multiprocessing.active_children()))
    for p in multiprocessing.active_children():
        print('Child process name:',p.name,' id:',p.pid)
    print('process ended')