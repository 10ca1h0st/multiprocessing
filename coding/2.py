#!/usr/bin/python

from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self,loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for i in range(self.loop):
            time.sleep(i)
            print(i)


if __name__ == '__main__':
    for i in range(2,6):
        p = MyProcess(i)
        p.daemon = True
        p.start()
        p.join()
    print('main process ended')

