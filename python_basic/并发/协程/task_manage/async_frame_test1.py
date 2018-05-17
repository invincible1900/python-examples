# coding:utf-8
# 功能: 扫描一个B段开放80和8080端口的网站并记录网页Title
# 一个这样的任务需要在一个独立的目录下
from task_manage.concurrent_frame_async import Concurrent, MyTimer
import asyncio
import aiohttp
import json
from netaddr import IPNetwork
from bs4 import BeautifulSoup

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
    def __init__(self, concurrent, event_loop, state_file='', save_mid_result=True, check_done=True):
        super(MyTask, self).__init__(concurrent, event_loop, state_file=state_file, save_mid_result=save_mid_result, check_done=check_done)
        connector = aiohttp.TCPConnector(loop=self.loop, verify_ssl=False)
        self.session = aiohttp.ClientSession(loop=self.loop, connector=connector)


    # 自定义任务执行方法
    @asyncio.coroutine
    def work(self, task):

        # 自定义的task对象的taskobj字段为url
        url = task['taskobj']
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
        }

        try:
            with aiohttp.Timeout(5):
                with MyTimer() as timer:

                    response = yield from self.session.get(url=url, headers=header, allow_redirects=False,)
                    # res = requests.get(url, headers=header, verify=False, timeout=5)
                    res_data = yield from response.read()
                    if res_data:
                        title = get_title(res_data.decode('utf-8'))
                        # 返回自定义的处理结果，模块会将其转换成结果字典对象
                        # 其'result'字段保存处理结果
                        return {'url': url, 'title': title}
                LOGGER.info('[+] ok {}s'.format(timer.total))
        except Exception as exception:
            # LOGGER.error('task: {}, error: {}'.format(task['taskid'], str(exception)))
            return None

    def handle_result(self):
        self.session.close()
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
    testip = '1.1.0.0/16'
    net = IPNetwork(testip)
    tasks = []
    # 构造保存任务对象的任务列表
    for port in ['80', '8080']:
        tasks += [{'taskid': str(ip) + '_' + port, 'taskobj': 'http://{}:{}'.format(str(ip), port)} for ip in net]

    # 任务初始化
    mytask = MyTask(concurrent=1000, event_loop=loop, state_file=str(net.network),save_mid_result=True, check_done=True)

    # 开始并发执行任务
    result = yield from mytask.start(tasks)

    # 保存任务完成返回的结果
    if result:
        try:
            with open('1.1.0.0.txt', 'wb') as f:
                f.write(json.dumps(result, indent=2).encode('utf-8'))
        except Exception as exception:
            print(exception)
            print(result)

if __name__ == '__main__':
    # loop的作用范围？
    loop.run_until_complete(main())
