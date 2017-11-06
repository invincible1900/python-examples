# coding:utf-8
# 不同的互斥锁作用于不同的代码块
import threading
import time

m1 = threading.Lock()
m2 = threading.Lock()

def a():
    while True:
        m1.acquire()
        print 'a'*100
        m1.release()
        time.sleep(1)

def b():
    while True:
        m1.acquire()
        print 'b'*100
        m1.release()
        time.sleep(1)

threads = [
    threading.Thread(target=a),
    threading.Thread(target=b)
]

for t in threads:
    t.start()
