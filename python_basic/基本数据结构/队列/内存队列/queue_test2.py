# coding:utf-8
# 测试一个很low的队列复制的方法
# 测队列的存取会不会影响task.join(),结果是会
# 解决办法是加上taskdone
from queue import Queue
import time
import threading
lock = threading.Lock()

taskq = Queue()

def do():
    while True:
        time.sleep(1)
        with lock:
            print(taskq.get())
        taskq.task_done()

taskq.put('1')
taskq.put('2')
taskq.put('3')
taskq.put('4')
taskq.put('5')

t = threading.Thread(target=do)
t.setDaemon(True)
t.start()

u = []
with lock:
    while not taskq.empty():
        u.append(taskq.get())
    for i in u:
        taskq.put_nowait(i)
        # 注释掉这里的task_done后面的join就会一直阻塞
        taskq.task_done()

print(taskq.join())
print('ok')