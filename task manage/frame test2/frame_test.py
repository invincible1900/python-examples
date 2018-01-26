# coding:utf-8
# 功能: 扫描一个B段开放80和8080端口的网站并记录网页Title
# 一个这样的任务需要在一个独立的目录下
from task_manage.concurrent_frame import Concurrent
import json
from netaddr import IPNetwork
import requests
from bs4 import BeautifulSoup

def get_title(html):
    s = BeautifulSoup(html, 'lxml')
    title = s.title.string
    return title

class MyTask(Concurrent):

    def work(self, task):
        url = task['taskobj']
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
        }

        try:
            res = requests.get(url, headers=header, verify=False, timeout=5)
            res_data = res.content.decode('utf-8')
            if res_data:
                title = get_title(res_data)
                return {'url': url, 'title': title}

        except:
            return None

    def handle_result(self):
        # 任务结束后，将结果以json形式保存
        fmt_result = {'data': []}

        # 获取结果队列中的结果对象
        while not self.results.empty():
            processResult = self.results.get()
            fmt_result['data'].append(processResult['result'])

        return fmt_result

if __name__ == '__main__':
    testip = '183.0.0.0/16'
    net = IPNetwork(testip)
    tasks = []
    for port in ['80', '8080']:
        tasks += [{'taskid': str(ip) + '_' + port, 'taskobj': 'http://{}:{}'.format(str(ip), port)} for ip in net]

    mytask = MyTask(concurrency=300, save_mid_result=True, check_done=True)

    result = mytask.start(tasks)

    if result:
        try:
            with open('183.0.0.0.txt', 'wb') as f:
                f.write(json.dumps(result, indent=2).encode('utf-8'))
        except Exception as exception:
            print(exception)
            print(result)

