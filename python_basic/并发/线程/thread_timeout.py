# coding:utf-8
"""
测试给线程的join设置超时

超时后，线程不会停止，

只是main线程不再阻塞在join那里，而是继续执行
"""
import threading
import time

def f():
    print('waiting...')
    time.sleep(10)
    print('done')

for i in range(100):
    t = threading.Thread(target=f)
    t.setDaemon(True)
    t.start()
    t.join(2)
    print(t.isAlive())
    for t in threading.enumerate():
        print(t)


