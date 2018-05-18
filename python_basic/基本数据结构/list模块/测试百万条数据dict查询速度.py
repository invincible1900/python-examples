# coding: utf-8
"""
需求时对百万级别的任务进行去重
"""
import  loghandler
from mytimer import MyTimer
from netaddr import IPNetwork
LOGGER = loghandler.setup_logging()

donetasks = {}
ports = range(80, 100)
net = IPNetwork('1.104.0.0/16')

# 构造待添加任务列表(130万)
with MyTimer() as timer:
    tasks = []
    for port in ports:
        tasks += [
            {
                'taskid': '{}_{}'.format(str(ip), port),
                'taskobj': {'url': 'http://{}:{}'.format(str(ip), port), 'ip': str(ip), 'port': port}
            }
            for ip in net
        ]
LOGGER.info(u'创建了%d条任务, 用时%ss' % (len(tasks), str(timer.total)))

# 构造已完成任务(100万条)列表
for task in tasks[:1000000]:
    donetasks[task['taskid']] = True

# 开始做任务去重
done_counter = 0
new_counter = 0
counter = 0
with MyTimer() as timer:
    for task in tasks:
        if task['taskid'] in donetasks.keys():
            done_counter += 1
        else:
            new_counter += 1

        # 如果不加这个判断速度会提高0.4s
        counter += 1
        if counter % 1000 == 0:
            print(u'已检测%d' % counter)
LOGGER.info(u'共有%d条任务，已完成%d条，新任务%d条。用时%ss' % (len(tasks), done_counter, new_counter, str(timer.total)))

