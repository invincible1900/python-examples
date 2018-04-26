# coding:utf-8

"""
超时时间是整个loop总的超时时间


"""
import asyncio
import aiohttp
import json

# import async_timeout
from netaddr import IPNetwork
from asyncio.queues import Queue
import time
from bs4 import BeautifulSoup
from asyncio import ProactorEventLoop
loop = ProactorEventLoop()
asyncio.set_event_loop(loop)


taskq = Queue()
resultq = Queue()
good_urls = []
bad_urls = []
counter = 0

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


def get_title(html):
    try:
        s = BeautifulSoup(html, 'lxml')
        title = s.title.string.strip()
        return title
    except:
        return ''


async def fetch(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
    }

    t1 = time.time()
    global counter
    async with aiohttp.ClientSession(headers=headers) as client:
        try:
            ret = await client.get(url=url, timeout=60)
            res_data = await ret.text()
            res_headers = dict(ret.headers) 
            status_code = ret.status
            # print(type(res_data))
        except Exception as e:
            # print(e)
            counter += 1
            t2 = time.time()
            print(time.ctime(), counter, url, 0, int(t2-t1))
            return None

        title = get_title(res_data)
        counter += 1
        t2 = time.time()
        print(time.ctime(), counter, url, len(res_data), int(t2-t1))
        return {'url': url, 'title': title, 'headers': res_headers, 'html': res_data, 'res_code': status_code}

async def worker():
    while True:
        task = await taskq.get()
        url = task['taskobj']['url']
        # print(url)
        res = await fetch(url)
        if res:
            res['ip'] = task['taskobj']['ip']
            res['port'] = task['taskobj']['port']
            resultq.put_nowait(res)
            taskq.task_done()
            return res
        taskq.task_done()

async def main(tasks):
	print(u'等待任务完成....')
	await taskq.join()

	for t in tasks:
		t.cancel()


if __name__ == '__main__':
	# tasks = []
	b_net = '202.82.0.0/16'
	# ports = [80, 81, 82, 83, 84, 85, 86, 87, 88, 89]
	ports = [80, 8080, 8000, 1080, 8060, 8083]
	for ip in list(IPNetwork(b_net))[1:-1]:
		for port in ports:
			taskid = '{}_{}'.format(ip, port)
			taskobj = {'ip': str(ip), 'port': port, 'url': 'http://{}:{}'.format(ip, port)}
			# tasks.append({'taskid': taskid, 'taskobj': taskobj})
			taskq.put_nowait({'taskid': taskid, 'taskobj': taskobj})


	print(u'共添加%d条任务' % taskq.qsize())
	with MyTimer() as timer:
		concurrency = 10000
		tasks = []
		for i in range(concurrency):
			t = asyncio.Task(worker(), loop=loop)

			tasks.append(t)
		print(u'任务添加成功')
		loop.run_until_complete(main(tasks))
	print(u'所有任务完成，用时 %ds' % timer.total)		
	results = {'data': []}
	while not resultq.empty():
		res = resultq.get_nowait()
		results['data'].append(res)
	with open('res.json', 'w') as f:
		f.write(json.dumps(results, indent=2))
    #
    # tasks = []
    #
    #
    # with MyTimer() as timer:
    #     for i in range(concurrency):
    #         url = urls[i]
    #         tasks.append(fetch(url))
    #
    #     loop.run_until_complete(asyncio.wait(tasks))
    #     loop.close()
    #
    # print(u'共%d个url, 成功下载%d个页面， 用时 %ds' % (len(urls), len(good_urls), timer.total))
    # with open('good_urls.txt', 'w') as f:
    #     f.write('\n'.join(good_urls))
    #
    # #
    # with open('bad_urls.txt', 'w') as f:
    #     f.write('\n'.join(bad_urls))
