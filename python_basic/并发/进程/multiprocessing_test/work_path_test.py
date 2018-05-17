# coding:utf-8
"""
测试多进程切换到不同工作目录
"""
import multiprocessing
import os
import time

def change_dir(path):
    print('current path: ', os.getcwd())
    time.sleep(1)
    os.chdir(path)
    print('current path: ', os.getcwd())
    time.sleep(10)

if __name__ == '__main__':

    p1 = multiprocessing.Process(target=change_dir, args=('testdir1',))
    p2 = multiprocessing.Process(target=change_dir, args=('testdir2',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

