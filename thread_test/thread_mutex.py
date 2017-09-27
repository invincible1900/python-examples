#coding:utf-8
#测试MUTEX
import threading
import time  
  
NUM  = 0 
MUTEX = threading.Lock()
def test_xc():  
	global NUM
	MUTEX.acquire()
	print 'This is thread' + str(NUM)
	NUM += 1 
	MUTEX.release()
	time.sleep(1)  

if __name__ == '__main__':  
    for i in xrange(5):  
        t = threading.Thread(target=test_xc)  
        t.start()  