# coding:utf-8
# 功能: 扫描一个B段开放80和8080端口的网站并记录网页Title
# 一个这样的任务需要在一个独立的目录下
from task_manage.concurrent_frame_async import Concurrent, MyTimer
import asyncio
import aiohttp
import json
from bs4 import BeautifulSoup
import random
from asyncio.windows_events import ProactorEventLoop
loop = ProactorEventLoop()
asyncio.set_event_loop(loop)

import logging
import loghandler
loghandler.setup_logging()
LOGGER = logging.getLogger()

# 获取html文本中的title
def get_title(html):
    s = BeautifulSoup(html, 'lxml')
    title = s.title.string
    return title


class MyTask(Concurrent):

    # 自定义任务执行方法
    @asyncio.coroutine
    def work(self, task):

        # 自定义的task对象的taskobj字段为url
        try:
            with aiohttp.Timeout(5):
                # with aiohttp.Timeout(2):
                with MyTimer() as timer:
                    s = random.randint(1, 10)
                    yield from asyncio.sleep(s)
            # print('[+] ok {}s'.format(timer.total))
            return {'res': '[+] ok {}s supposed: {}s'.format(timer.total, s)}

        except Exception as exception:
            print('[-] error:{}'.format(str(exception)))
            return None


    def handle_result(self):
        # 任务结束后，将结果以json形式保存
        fmt_result = {'data': []}

        # 获取结果队列中的结果对象
        while not self.results.empty():
            processResult = self.results.get_nowait()

            # 获取所有处理结果
            fmt_result['data'].append(processResult['result'])

        return fmt_result

@asyncio.coroutine
def main():
    # 构造保存任务对象的任务列表
    tasks = [{'taskid': str(i) , 'taskobj': ''} for i in range(100000)]

    # 任务初始化
    mytask = MyTask(concurrent=1000, event_loop=loop, state_file='test3',save_mid_result=True, check_done=True)

    # 开始并发执行任务
    result = yield from mytask.start(tasks)

    # 保存任务完成返回的结果
    if result:
        try:
            with open('test3.txt', 'wb') as f:
                f.write(json.dumps(result, indent=2).encode('utf-8'))
        except Exception as exception:
            print(exception)
            print(result)

if __name__ == '__main__':
    # loop的作用范围？
    loop.run_until_complete(main())
