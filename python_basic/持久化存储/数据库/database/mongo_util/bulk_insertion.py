#coding:utf-8
from pymongo import MongoClient
from pymongo import InsertOne
import time

db_name = 'dbname'
col_name = 'collectionname'

mc = MongoClient("127.0.0.1", maxPoolSize=None)
db = mc[db_name]

def insert():
    # 批量写
    for i in range(0,255*255*255, 255*255):
        data = {
            'k': 'v'
        }
        res = [InsertOne(data) for _ in range(255*255)]

        print('writing...')
        db[col_name].bulk_write(res)


