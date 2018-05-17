# coding:utf-8

import time
t = time.time()
f = open(u'大文件路径','rb')
print(f)
data = f.read(1024*1024*500)
data2 = f.read(1024*1024*500)
print(len(data), time.time()-t)

