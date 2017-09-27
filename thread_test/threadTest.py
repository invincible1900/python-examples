#coding:utf-8
# 测试线程的运行过程
import threading
from time import ctime,sleep


def music(func):
    for i in range(12):
        print "I'm listening to %s. %s" %(func,ctime())
        sleep(1)

def movie(func):
    for i in range(12):
        print "I'm' watching the %s! %s" %(func,ctime())
        sleep(5)

threads = []
t1 = threading.Thread(target=music,args=(u'Carry on',))
threads.append(t1)
t2 = threading.Thread(target=movie,args=(u'Avatar',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        # t.setDaemon(True)
        t.start()

    print "all over %s" %ctime()
    # raw_input()