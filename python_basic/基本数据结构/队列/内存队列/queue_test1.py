# coding:utf-8

# 测试是否可以join两次
# 能
from queue import Queue
import threading
import time

def do():
    while True:
        time.sleep(5)
        print(taskq.get())
        taskq.task_done()

taskq = Queue()

taskq.put('1')
taskq.put('2')
taskq.put('3')

t = threading.Thread(target=do)
t.setDaemon(True)
t.start()

print(taskq.join())
print('ok')
print(taskq.join())
print(taskq.join())
print(taskq.join())
print('done')


# 测taskq能不能copy
# 不能
from queue import Queue

taskq = Queue()

taskq.put('1')
taskq.put('2')
taskq.put('3')

# nq = taskq.copy()