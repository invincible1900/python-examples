# coding:utf-8
# 测试目标: 腾讯云主机

# 测试数据：
# 本机运行，超时0.1s 并发500 全端口速度在30s左右，准确率较高
# 本机运行，超时0.3s 并发1000 全端口速度在40s左右，准确率较高
# 本机运行，超时1s 并发1000 全端口速度在90s左右，准确率较高
# 并发量越少，浪费在cpu在协程间切换的时间就越少，效率越高
# 超时越长准确率越高


# 考虑因素：
# 1. 与目标的网络延时，延时小的时候设置更小的超时时间，减少并发量
# 2. 与目标的网络延时，延时高的时候设置较大的超时时间，增加并发量
# 3. CPU性能高时候，增加并发量

import json
import asyncio
from asyncio import ProactorEventLoop
from socket import *
import time
import async_timeout

loop = ProactorEventLoop()
asyncio.set_event_loop(loop)

result = {}

class MyTimer(object):
    """
    利用上下文管理器封装的一个对代码块执行时间计时器

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

async def port_sacn(ip, port):
    s = socket(AF_INET, SOCK_STREAM)
    t1 = time.time()
    try:
        with async_timeout.timeout(1):
            ret = await loop.sock_connect(s, (ip, port))
        t2 = time.time()

        if ret:
            s.close()
            result[port] = {'status': 'open', 'res_time': str(t2-t1)[:4]}
            print(time.ctime(), port, 'open', str(t2-t1)[:4])
        else:
            s.close()
            result[port] = {'status': 'close', 'res_time': str(t2 - t1)[:4]}
            # print(time.ctime(), port, 'close', str(t2-t1)[:4])
    except:
        s.close()
        t2 = time.time()
        result[port] = {'status': 'close', 'res_time': str(t2 - t1)[:4]}
        # print(time.ctime(), port, 'close', str(t2-t1)[:4])


if __name__ == '__main__':
    ip = '192.168.1.1'
    concurrency = 1000
    times = int(65535/concurrency)
    counter = 0

    with MyTimer() as timer:
        for _ in range(times):
            tasks = []
            
            for _ in range(concurrency):
                counter += 1
                port = counter
                tasks.append(asyncio.Task(port_sacn(ip, port), loop=loop))

            loop.run_until_complete(asyncio.wait(tasks))

        tasks = [asyncio.Task(port_sacn(ip, port), loop=loop) for port in range(counter+1, 65536)]
        loop.run_until_complete(asyncio.wait(tasks))

    print(u'任务完成,用时 %ds' % timer.total)

    order_result = {}
    for k in sorted(result.keys(), reverse=False):
        order_result[k] = result[k]


    with open(ip + '_scan_res.json', 'w') as f:
        f.write(json.dumps(order_result, indent=2))