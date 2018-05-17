import threading
import time
M = threading.Lock()

def fun():
	M.acquire()
	print 'test thread',threading.currentThread()
	time.sleep(1)
	M.release()


threads = [threading.Thread(target=fun) for _ in range(10)]
for t in threads:t.start()
for t in threads:t.join()
for _ in range(50):
	time.sleep(2)
	with open('test.txt','a') as f:
		f.write('test')
