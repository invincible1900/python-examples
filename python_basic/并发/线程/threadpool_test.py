# coding:utf-8
# threading + queue实现的简单线程池

import time
import threading
import queue


class WorkThread(threading.Thread):
    """工作线程类
    """
    def __init__(self, work_queue):
        """工作线程类初始化函数
        """
        threading.Thread.__init__(self)
        self._work_queue = work_queue #线程同步队列
        self.setDaemon(True) #主线程退出后，子线程也退出
        self.start()

    def run(self):
        """任务接口
        """
        while True:
            try:
                func, args = self._work_queue.get()
                func(args)
                self._work_queue.task_done()
            except Exception as reason:
                print(reason)
                break


class ThreadPool(object):
    """线程池管理类
    """
    def __init__(self, concurrency = 1):
        """线程池管理器初始化函数

        Args:
            thread_count: 线程池中的线程个数
        """
        self._concurrency = concurrency
        self._work_queue = queue.Queue()
        self._threads = []
        self.init_threads_pool()

    def init_threads_pool(self):
        """建立并启动thread_count个线程
        """
        for index in range(self._concurrency):
            self._threads.append(WorkThread(self._work_queue))

    def add_work(self, function, param):
        """增加新任务。 (调用函数，参数)
        """
        self._work_queue.put((function, param))

    def wait_queue_empty(self):
        """等待队列为空。某些场景下可等同于所有任务均执行完
        """
        self._work_queue.join()

def work_func(num):
    """测试函数，在控制台打印num
    """
    print(num)
    time.sleep(3)

def main():
    """Thread_Pool使用例子
    """
    thread_count = 5
    thread_pool = ThreadPool(thread_count)
    for num in range(0, 100):
        thread_pool.add_work(work_func, num) #添加任务
    thread_pool.wait_queue_empty() #等待任务执行完

    print("---end---")

if __name__ == "__main__":
    main()