from task_manage.concurrent_frame import Concurrent
import json
from netaddr import IPNetwork
import requests

class MyTask(Concurrent):

    def work(self, task):
        ip = task['taskobj']
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
        }

        key = 'TSTRoinK6sOCXdqsoIRUVN7paGVcWT8OcXxgnmSYoKovApoLcs7ZHe5jujDv0NA2'
        url = 'https://mall.ipplus360.com/ip/locate/api?key=%s&ip=%s&coordsys=BD09' % (key, ip)

        try:
            res = requests.get(url, headers=header, verify=False)
            res_data = res.content.decode('utf-8')
            jdata = json.loads(res_data)

            if jdata['code'] == 200:
                return jdata
        except:
            pass

    def handle_result(self):
        # 任务结束后，将结果以json形式保存
        fmt_result = {'data': []}

        # 获取结果队列中的结果对象
        while not self.results.empty():
            processResult = self.results.get()

            # 提取结果对象的处理结果，并构造成需要的形式
            dataUnit = {'ip': processResult['result']['ip'], 'info': processResult['result']['data']}

            fmt_result['data'].append(dataUnit)

        return fmt_result

if __name__ == '__main__':
    testip = '183.0.0.0/16'
    net = IPNetwork(testip)
    tasks = [{'taskid': str(ip), 'taskobj': str(ip)} for ip in net]
    mytask = MyTask(concurrency=1, save_mid_result=True, check_done=True)
    result = mytask.start(tasks)
    if result:
        try:
            with open('183.0.0.0.txt', 'wb') as f:
                f.write(json.dumps(result, indent=2).encode('utf-8'))
        except Exception as exception:
            print(exception)
            print(result)

