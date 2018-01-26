# coding:utf-8
import os
from queue import Queue
import threading
import time
import json
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.urllib3.disable_warnings(InsecureRequestWarning)


# 利用上下文管理器封装的一个对代码块执行时间记录的计时器
class MyTimer(object):
    def __init__(self):
        self.start = 0
        self.end = 0
        self.total = 0

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.total = self.end - self.start


# 处理文件操作的类
class FileHandler:
    def __init__(self):
        if not os.path.exists('state'):
            os.mkdir('state')

        # 用于状态保存的文件
        self.donefilename = 'state/done.txt'
        self.failedfilename = 'state/failed.txt'
        self.cachefilename = 'state/cache.txt'

        # 每条缓存数据的间隔符（可自定义，类似POST的boundary）
        self.boundary = '\n\n'

        # 文件读写线程锁
        self.lock = threading.Lock()

    # 记录已完成的任务的taskid列表
    def record_done_task(self, task):
        taskid = task['taskid']
        with self.lock:
            with open(self.donefilename, 'a') as f:
                f.write(str(taskid) + '\n')

    # 返回完成的任务taskid列表
    def read_done_tasks(self):
        with self.lock:
            with open(self.donefilename, 'r') as f:
                donetasks = f.readlines()
        return donetasks

    # 记录失败的任务的taskid列表
    def record_failed_task(self, task):
        taskid = task['taskid']
        with self.lock:
            with open(self.failedfilename, 'a') as f:
                f.write(str(taskid) + '\n')

    # 返回失败的任务taskid列表
    def read_error(self):
        with self.lock:
            with open(self.cachefilename, 'r') as f:
                error_tasks = f.readlines()
        return error_tasks

    # 保存缓存数据对象
    def record_cache(self, data):
        # 每条记录添加分隔符号
        data += self.boundary

        with self.lock:
            with open(self.cachefilename, 'ab') as f:
                f.write(data.encode('utf-8'))

    # 返回缓存数据对象列表
    def read_cache(self):
        with self.lock:
            with open(self.cachefilename, 'rb') as f:
                cachedata = f.read().decode('utf-8')
        return [json.loads(data) for data in cachedata.split(self.boundary)]


class Concurrent:
    def __init__(self, concurrency=10, save_mid_result=True):
        # 设置工作单元的并发个数
        self.concurrency = concurrency

        # 任务队列
        self.tasks = Queue()

        # 结果队列
        self.results = Queue()

        # 线程互斥锁
        self.lock = threading.Lock()

        # 文件处理类实例
        self.fh = FileHandler()

        # 设置是否缓存处理结果数据
        # 若不想保存缓存数据则设置save_mid_result参数为False
        self.save_mid_result = save_mid_result

        # 结果队列的数据对象
        self.result = {'taskid':'', 'result': ''}

        # 任务的对象
        self.task = {'taskid': '', 'taskobj': ''}

        # 缓存数据对象
        self.cache = {'taskid': '', 'cachedata': ''}

    # 并发执行任务，并保存结果到队列的工作单元
    def worker(self):
        while True:
            try:
                # 取出任务
                one_task = self.tasks.get()

                # 处理任务
                process_result = self.process(one_task)

                # 转换成结果对象
                result = self.result.copy()
                result['taskid'] = one_task['taskid']
                result['result'] = process_result

                # 处理结果入栈
                self.results.put(result)

                # 入栈的同时，保存到文件
                if self.save_mid_result:
                    # 将处理结果封装成缓存数据对象
                    mid_result = self.cache.copy()
                    mid_result['taskid'] = one_task['taskid']
                    mid_result['cachedata'] = process_result

                    # 将记录保存
                    self.fh.record_cache(json.dumps(mid_result, indent=2))

            except Exception as exception:
                # 任务失败
                self.fh.record_failed_task(one_task)
                print(exception)
            finally:
                # 任务完成
                self.tasks.task_done()
                self.fh.record_done_task(one_task)


    # 根据并发数，创建并启动线程
    # 并发数决定了同一时刻最多同时运行的线程数
    def create_threads(self):
        for _ in range(self.concurrency):
            t = threading.Thread(target=self.worker)
            t.setDaemon(True)
            t.start()


    # 处理数据量不大时的查重
    def is_done(self, task):
        taskid = task['taskid']
        donetasks = self.fh.read_done_tasks()
        if taskid in donetasks:
            return True
        else:
            return False


    # 向任务队列中添加任务,根据具体任务自定义
    # 任务对象为字典，需要包含至少taskid和taskobj两个字段
    # 分别是一个任务的唯一标识，和任务内容
    def add_job(self, task, check_done):
        if check_done:
            if self.is_done(task):
                self.tasks.put(task)
                return True
        else:
            self.tasks.put()
            return True

        return False

    def add_jobs(self, tasks, check_done=True):
        todo = 0
        for task in tasks:
            if self.add_job(task, check_done):
                todo += 1
        print('Got {} tasks to do.'.format(todo))

    def main(self):
        with MyTimer() as timer:
            # 启动工作线程
            self.create_threads(self.concurrency)

            # 添加任务
            self.add_jobs()

            # 阻塞直到所有任务结束
            print('Waiting...\n')
            self.tasks.join()

            # 处理结果
            self.handle_result()

        print('\nAll task done after {}s.'.format(int(timer.total)))


    def get_res_from_local(self, task):
        taskid = task['taskid']
        cachedatas = self.fh.read_cache()
        if cachedatas:
            for data in cachedatas:
                if taskid == data['taskid']:
                    return data['cachedata']
        return None

    def process(self, task, check_local=True):
        if check_local:
            res = self.get_res_from_local(task)
            if res:
                return res

        return self.work(task)

    # 自定义处理任务的函数，一般为阻塞的IO操作
    def work(self):
        raise NotImplementedError


    # 处理结果
    def handle_result(self):
        raise NotImplementedError


if __name__ == '__main__':
    pass



