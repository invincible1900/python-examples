# coding:utf-8
import pymongo

db_name = 'routerScan'
col_name = 'scanResult'

# 连接数据库服务器
client = pymongo.MongoClient('localhost', 27017)


db = client[db_name]
col = db[col_name]
col.remove({})

# 关闭连接
client.close()
