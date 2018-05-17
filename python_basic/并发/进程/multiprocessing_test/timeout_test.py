# coding:utf-8
"""
测试多进程的join设置超时

结果同多线程的join超时

子进程会继续运行，但是主进程不会继续在join出阻塞

"""
import multiprocessing
import os
import time

def timer(tag):
    for i in range(10):
        time.sleep(1)
        print(tag, i)

if __name__ == '__main__':

    p1 = multiprocessing.Process(target=timer, args=('p1',))
    p2 = multiprocessing.Process(target=timer, args=('p2',))

    p1.start()
    p2.start()
    p1.join(timeout=3)
    print('p1 done')
    p2.join()
    print('p2 done')
