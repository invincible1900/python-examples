#coding:utf-8
#测试线程嵌套
import threading
import time
def a():
    while True:
        print 'a'
        time.sleep(3)

        t = threading.Thread(target=b)
        t.setDaemon(True)
        t.start()

def b():
    print 'b'
    time.sleep(8)

def main():
    print 'main'
    time.sleep(5)

t = threading.Thread(target=a)
t.setDaemon(True)
t.start()

while True :
    main()
