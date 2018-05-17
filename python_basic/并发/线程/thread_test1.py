# coding:utf-8
# 线程类的实现
# MUTEX线程锁的基本使用
import time
import threading
MUTEX = threading.Lock()

class TThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(True)

    def run(self):
        for _ in range(10):
            time.sleep(1)
            with MUTEX:
                print( 'message from %s' % threading.currentThread().getName())


threads = [TThread() for _ in range(10)]
for t in threads:
    t.start()

for t in threads:
    t.join()