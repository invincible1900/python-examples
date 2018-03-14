# coding:utf-8
import pymongo

db_name = 'routerScan'
col_name = 'scanResult'

# 连接数据库服务器
client = pymongo.MongoClient('localhost', 27017)

db = client[db_name]
db.create_collection(col_name)

# 关闭连接
client.close()