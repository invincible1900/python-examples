#coding:utf-8
from pymongo import MongoClient
from pymongo import InsertOne
import time
import threading
import base64

mc = MongoClient("127.0.0.1", maxPoolSize=None)
db = mc['test']

def insert(tid):

    # 逐条写
    # t0 = time.time()
    # for i in range(0,100**4):
    #     db['test_1'].insert_one({'_id':i,'x':1})
    # print (time.time() - t0)
    #
    # time.sleep(1)

    # 批量写
    t0 = time.time()
    res =[]
    for i in range(0,255*255*255):
        data = {
            '_id': base64.b64encode((str(i) + tid).encode('utf-8')),
            'taskId': 0,
            'taskObject': {
                "region": '',
                'url': '',
                'ip': '',
                'port': ''
            },
            'handleResult': {
                'brand': '',
                'username': '',
                'password': '',
                "latitude": "",
                "longitude": "",
                "addr1": "",
                "addr2": "",
            },
            'status': 0,
            'reprocessing': False,
            'cacheData': '',
            'errorMessage': ''
        }
        res.append(InsertOne(data))
        if len(res) >= 255*255:
            print('writing...')
            db['test_2'].bulk_write(res)
            res = []

    print (time.time() - t0)


if __name__ == '__main__':
    # threads = [threading.Thread(target=insert, args=('thread' + str(i),)) for i in range(3)]
    # for t in threads:
    #     t.start()
    #
    # for t in threads:
    #     t.join()
    # insert('t1')
    i = 1
    tid = 'abc'
    data = {
        '_id': base64.b64encode((str(i) + tid).encode('utf-8')),
        'taskId': 0,
        'taskObject': {
            "region": '',
            'url': '',
            'ip': '',
            'port': ''
        },
        'handleResult': {
            'brand': '',
            'username': '',
            'password': '',
            "latitude": "",
            "longitude": "",
            "addr1": "",
            "addr2": "",
        },
        'status': 0,
        'reprocessing': False,
        'cacheData': '',
        'errorMessage': ''
    }
    print(len(data) * 255*255*255/1024/1024)