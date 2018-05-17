# coding:utf-8
import os
from queue import Queue
import threading
import time
import json
import logging
LOGGER = logging.getLogger()


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
    def __init__(self, state_file_name=''):

        # 创建状态保存目录
        self.state_path = state_file_name + '_state'
        if not os.path.exists(self.state_path):
            os.mkdir(self.state_path)

        # 用于状态保存的文件
        self.donefilename = self.state_path + '/done.txt'
        self.failedfilename = self.state_path + '/failed.txt'
        self.cachefilename = self.state_path + '/cache.txt'

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

            ret = data.decode(coding).split(self.boundary)
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
        cachedatas =  self._read_file(self.cachefilename, coding)
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
    def __init__(self, concurrency=10, state_file='', save_mid_result=True, check_done=True):
        # 设置工作单元的并发个数
        self.concurrency = concurrency

        # 任务队列
        self.tasks = Queue()

        # 结果队列
        self.results = Queue()

        # 线程互斥锁
        self.lock = threading.Lock()

        # 文件处理类实例
        self.fh = FileHandler(state_file_name=state_file)

        # 设置是否缓存处理结果数据
        self.save_mid_result = save_mid_result

        # 设置是否进行任务去重
        self.check_done = check_done

        # 结果数据对象
        self.result = {'taskid': '', 'result': ''}

        # 任务对象
        self.task = {'taskid': '', 'taskobj': ''}

        # 初始化完成列表
        self.donetasks = {}
        if self.check_done:
            ds = self.fh.read_done_tasks()
            if ds:
                for i in ds:
                    self.donetasks[i] = True

        # 加入队列的任务数
        self.todo = 0

        # 完成任务数
        self.complete = 0.0

        # 完成度
        self.completion = 0.0

    def process(self, task):
        """
        任务处理
        :param task: 任务对象
        :return: 任务的处理结果对象
        """
        # if self.check_local:
        #     # 从本地缓存中获取结果对象
        #     result = self.get_res_from_local(task)
        #     if not result:
        # 执行用户定义的任务处理函数
        work_res = self.work(task)
        if work_res:

            # 把用户自定义函数的处理结果封装成结果对象
            result = self.result.copy()
            result['taskid'] = task['taskid']
            result['result'] = work_res

            # 将结果保存到缓存文件
            if self.save_mid_result:
                # LOGGER.info(result)
                self.fh.record_cache(result)

                return result

    def load_cache(self):
        # LOGGER.info('loading cache data...')
        LOGGER.info(u'加载缓存数据...')
        cachedatas = self.fh.read_cache()
        if cachedatas:
            for data in cachedatas:
                self.results.put(data)
                try:
                    LOGGER.debug(json.dumps(data))
                except:
                    LOGGER.exception(u'缓存数据日志打印异常')

        # LOGGER.info('cache data loaded.')
        if cachedatas:
            LOGGER.info(u'缓存数据加载完成，共加载%d条数据.' % len(cachedatas))
        else:
            LOGGER.info(u'缓存数据加载完成，共加载0条数据.')

    def worker(self):
        """
        并发任务单元，执行任务，并将结果保存到结果队列
        :return: None
        """
        while True:
            if self.get_proportion():
                LOGGER.info(u'任务当前完成进度: %d%%' % (self.completion * 100))
            try:
                # 取出任务
                one_task = self.tasks.get()
                # LOGGER.debug(u'获取任务%s' % one_task['taskid'])

                # 处理任务
                process_result = self.process(one_task)
                # LOGGER.info(str(process_result))

                # 未得到处理结果当做失败处理
                if not process_result:
                    # LOGGER.debug(u'处理结果为空，任务%s失败' % one_task['taskid'])
                    self.fh.record_failed_task(one_task)
                    with self.lock:
                        self.complete += 1
                    continue

                # 处理结果入栈
                self.results.put(process_result)
                with self.lock:
                    self.complete += 1
                    print(json.dumps(process_result))
                # try:
                #     LOGGER.debug(u'%s处理结果入栈' % one_task['taskid'])
                #     LOGGER.debug(json.dumps(process_result))
                # except:
                #     LOGGER.exception(u'结果数据日志打印异常')

            except:
                # 任务失败
                with self.lock:
                    self.complete += 1

                self.fh.record_failed_task(one_task)
                # LOGGER.exception('worker error.')
                LOGGER.exception(u'worker未知异常')
                continue

            finally:
                # 任务完成
                self.tasks.task_done()
                self.fh.record_done_task(one_task)
                # LOGGER.debug(u'任务%s结束' % one_task['taskid'])

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
        if self.donetasks and taskid in self.donetasks.keys():
            return True
        else:
            return False

    def add_job(self, task):
        """
        向任务队列中添加一个任务
        :param task: 字典对象，格式：{'taskid': '', 'taskobj': ''}，taskid 为代表任务对象的唯一字符串标识，taskobj 为自定义的任务对象。
        :return: 若添加任务返回True,未添加任务返回False
        """
        # LOGGER.debug(u'正在检测%s' % task['taskid'])
        if self.check_done and self.is_done(task):
                return False
        else:
            self.tasks.put(task)
            return True

    def add_jobs(self, tasks):
        """
        将所有任务对象添加到任务队列
        :param tasks: 任务列表，列表元素为任务对象
        :return: None
        """
        # LOGGER.info('Adding new tasks...')
        LOGGER.info(u'添加新任务...')
        # handle_counter = float(0)
        # proportion = 0.0
        for task in tasks:
            # handle_counter += 1
            # if handle_counter/len(tasks) >= 0.2 and proportion < 0.2:
            #     LOGGER.info(u'已完成20%...')
            #     proportion = 0.2
            # if handle_counter/len(tasks) >= 0.4 and proportion < 0.4:
            #     LOGGER.info(u'已完成40%...')
            #     proportion = 0.4
            # if handle_counter/len(tasks) >= 0.6 and proportion < 0.6:
            #     LOGGER.info(u'已完成60%...')
            #     proportion = 0.6
            # if handle_counter/len(tasks) >= 0.8 and proportion < 0.8:
            #     LOGGER.info(u'已完成80%...')
            #     proportion = 0.8

            if self.add_job(task):
                self.todo += 1
        # LOGGER.info('Got {} tasks to do.'.format(todo))
        LOGGER.info(u'添加完成，共获得{}条任务.'.format(self.todo))

    def get_proportion(self):
        """
        获取当前任务占比
        :return: 返回True表示比例更新
        """

        with self.lock:
            if self.todo == 0:
                self.completion = 1
                return False

            for i in range(1, 101):
                if self.complete / float(self.todo) >= i / 100.0 > self.completion:
                    self.completion = i / 100.0
                    return True
                else:
                    continue

    def start(self, tasks):
        """
        启动任务
        :param tasks: 任务列表，列表元素为任务对象
        :return: 若自定义的handle_result函数有返回值则将之返回，否则返回None
        """

        with MyTimer() as timer:
            # 读取缓存数据
            self.load_cache()

            # 添加任务
            self.add_jobs(tasks)

            # 启动工作线程
            self.create_threads()

            # 阻塞直到所有任务结束
            # LOGGER.info('Waiting...')
            LOGGER.info(u'等待任务结束...')
            self.tasks.join()

            # 处理结果
            handle_res = self.handle_result()

        # LOGGER.info('All task done after {}s.'.format(int(timer.total)))
        LOGGER.info(u'所有任务已结束，用时 {}s.'.format(int(timer.total)))

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



