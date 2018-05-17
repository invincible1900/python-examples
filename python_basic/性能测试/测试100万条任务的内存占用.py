# coding:utf-8
"""
10万条占用内容31K左右
100万条227K
1000万条2000K + 程序MemoryError退出
"""
from queue import Queue
q = Queue()
# 10万
# total = 100000

# 100万
total = 1000000

# 1000万
# total = 10000000


for i in range(total):
    task = {'taskid': str(i), 'taskobj': 'http://www.%d.com' % i}
    q.put_nowait(task)

print(u'添加完成')
import time
time.sleep(100)