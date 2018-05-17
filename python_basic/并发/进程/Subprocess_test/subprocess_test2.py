#coding=utf-8
from multiprocessing import Process
import os

# 子进程要执行的代码
def fun_proc(name):
    script = r'python test_file.py'
    os.popen(script)


if __name__=='__main__':
    print('父进程 %d' % os.getpid())
    p = Process(target=fun_proc, args=('我是子进程',))
    print('子进程将要执行')
    p.start()
    # p.join()
    print('子进程已结束')
# 结果如下：
# 父进程 11876
# 子进程将要执行
# 子进程运行中，name= 我是子进程 ,pid=14644
# 子进程已结束

