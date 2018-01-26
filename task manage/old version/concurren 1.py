# coding:utf-8
# concurrent.py
import os
from queue import Queue
import threading
import time
import json


class MyTimer(object):
    """
    利用上下文管理器封装的一个对代码块执行时间记录的计时器

    """
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

class FileHandler:
    """
    处理文件操作的类

    """
    def __init__(self):

        # 创建状态保存目录
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

    def _save_to_file(self, filename, data, coding='utf-8'):
        """
        将字符串添加分隔符保存到文件
        :param filename: 文件路径
        :param data: 字符串类型数据
        :param coding: 保存的编码类型
        :return: None
        """

        # 为每条记录添加分隔符
        data += self.boundary

        with self.lock:
            with open(filename, 'ab') as f:
                f.write(data.encode(coding))

    def _read_file(self, filename, coding='utf-8'):
        """
        将文件内容由boundary分割成列表返回
        :param filename: 文件路径
        :param coding: 文件编码
        :return: 若文件不存在返回None，否则返回字符串列表
        """
        if os.path.exists(filename):
            with self.lock:
                with open(filename, 'rb') as f:
                    data = f.read()

            ret = data.decode('utf-8').split(self.boundary)
            return ret
        else:
            return None

    def record_done_task(self, task):
        """
        记录已完成的任务的taskid列表
        :param task: 字典类型的任务对象{'taskid': '', 'taskobj': ''}
        :return: None
        """

        self._save_to_file(self.donefilename, task['taskid'])

    def read_done_tasks(self):
        """
        读取完成的任务taskid列表
        :return: 完成的任务taskid列表
        """

        return self._read_file(self.donefilename)

    def record_failed_task(self, task):
        """
        记录失败的任务的taskid列表
        :param task: 字典类型的任务对象{'taskid': '', 'taskobj': ''}
        :return: None
        """
        self._save_to_file(self.failedfilename, task['taskid'])

    def read_failed_tasks(self):
        """
        获取失败的任务taskid列表
        :return: 失败的任务taskid列表
        """
        return self._read_file(self.failedfilename)

    def record_cache(self, data, coding='utf-8'):
        """
        保存缓存数据对象
        :param coding: 文件的编码类型
        :param data: 字典类型的结果对象{'taskid': '', 'result': ''}
        :return: None
        """
        data = json.dumps(data, indent=2)
        self._save_to_file(self.cachefilename, data, coding)

    def read_cache(self, coding='utf-8'):
        """
        返回缓存数据列表
        :param coding: 文件编码类型
        :return: 字典类型的结果对象{'taskid': '', 'result': ''}列表
        """
        cachedatas = self._read_file(self.cachefilename, coding)
        if cachedatas:
            return [json.loads(data.strip()) for data in cachedatas if data.strip()]
        else:
            return None

    def clear_chache(self):
        """
        清除缓存
        :return: None
        """
        os.remove(self.cachefilename)

    def clear_done_tasks(self):
        """
        清除完成任务列表
        :return: None
        """
        os.remove(self.donefilename)

    def clear_error_tasks(self):
        """
        清除失败任务列表
        :return: None
        """
        os.remove(self.failedfilename)

class Concurrent:
    """
    实现该类的work和handle_result函数，并指定一个任务列表，可以并发的处理任务。并且带有状态保存，任务去重，数据缓存等功能。

    任务列表中的数据为字典对象，字典格式：{'taskid': '', 'taskobj': ''}，taskid 为代表任务对象的唯一字符串标识，taskobj 为自定义的任务对象。

    """
    def __init__(self, concurrency=10, save_mid_result=True, check_local=True):
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
        self.save_mid_result = save_mid_result

        # 设置是否先从本地缓存中查找数据
        self.check_local = check_local

        # 结果数据对象
        self.result = {'taskid': '', 'result': ''}

        # 任务对象
        self.task = {'taskid': '', 'taskobj': ''}

    def get_res_from_local(self, task):
        """
        从本地缓存中获取结果对象
        :param task: 任务对象
        :return: 若结果存在则返回结果对象，若不存在返回None
        """
        taskid = task['taskid']
        cachedatas = self.fh.read_cache()
        if cachedatas:
            for data in cachedatas:
                if taskid == data['taskid']:
                    return data
        return None

    def process(self, task, check_local=True):
        """
        任务处理
        :param task: 任务对象
        :param check_local: 是否尝试从本地缓存获取处理结果
        :return: 任务的处理结果对象
        """
        if check_local:
            # 从本地缓存中获取结果对象
            result = self.get_res_from_local(task)
            if not result:
                # 执行用户定义的任务处理函数
                work_res = self.work(task)
                if work_res:

                    # 把用户自定义函数的处理结果封装成结果对象
                    result = self.result.copy()
                    result['taskid'] = task['taskid']
                    result['result'] = work_res

                    # 将结果保存到缓存文件
                    if self.save_mid_result:
                        self.fh.record_cache(result)

            return result


    def worker(self):
        """
        并发任务单元，执行任务，并将结果保存到结果队列
        :return: None
        """
        while True:
            try:
                # 取出任务
                one_task = self.tasks.get()

                # 处理任务
                process_result = self.process(one_task)

                # 未得到处理结果当做失败处理
                if not process_result:
                    self.fh.record_failed_task(one_task)
                    continue

                # 处理结果入栈
                self.results.put(process_result)

            except Exception as exception:
                # 任务失败
                self.fh.record_failed_task(one_task)
                print(exception)
                continue

            finally:
                # 任务完成
                self.tasks.task_done()
                self.fh.record_done_task(one_task)

    def create_threads(self):
        """
        根据并发数，创建并启动线程,并发数决定了同一时刻最多同时运行的线程数
        :return: None
        """
        for _ in range(self.concurrency):
            t = threading.Thread(target=self.worker)
            t.setDaemon(True)
            t.start()

    def is_done(self, task):
        """
        处理数据量不大时的任务去重
        :param task:
        :return: 若任务已经执行返回True,否则返回False
        """
        taskid = task['taskid']
        donetasks = self.fh.read_done_tasks()
        if donetasks and taskid in donetasks:
            return True
        else:
            return False

    def add_job(self, task, check_done):
        """
        向任务队列中添加一个任务
        :param task: 字典对象，格式：{'taskid': '', 'taskobj': ''}，taskid 为代表任务对象的唯一字符串标识，taskobj 为自定义的任务对象。
        :param check_done: 添加任务前是否进行去重
        :return: 若添加任务返回True,未添加任务返回False
        """
        if check_done and self.is_done(task):
                return False
        else:
            self.tasks.put(task)
            return True

    def add_jobs(self, tasks, check_done=True):
        """
        将所有任务对象添加到任务队列
        :param tasks: 任务列表，列表元素为任务对象
        :param check_done: 设置添加任务前是否进行去重
        :return: None
        """
        todo = 0
        for task in tasks:
            if self.add_job(task, check_done):
                todo += 1
        print('Got {} tasks to do.'.format(todo))

    def start(self, tasks):
        """
        启动任务
        :param tasks: 任务列表，列表元素为任务对象
        :return: 若自定义的handle_result函数有返回值则将之返回，否则返回None
        """
        with MyTimer() as timer:
            # 启动工作线程
            self.create_threads()

            # 添加任务
            self.add_jobs(tasks)

            # 阻塞直到所有任务结束
            print('Waiting...\n')
            self.tasks.join()

            # 处理结果
            handle_res = self.handle_result()

        print('\nAll task done after {}s.'.format(int(timer.total)))

        return handle_res

    def work(self, task):
        """
        自定义处理任务的函数，一般为阻塞的IO操作
        :param task: 字典对象，格式：{'taskid': '', 'taskobj': ''}，taskid 为代表任务对象的唯一字符串标识，taskobj 为自定义的任务对象
        :return: 任意类型的任务处理结果，若返回None表示未获取到结果
        """
        raise NotImplementedError

    def handle_result(self):
        """
        自定义结果处理函数，从结果队列中读取结果对象，并进行处理
        :return: 自定义
        """
        raise NotImplementedError

if __name__ == '__main__':
    pass