# coding:utf-8
import pymongo

db_name = 'test'
col_name = 'test_2'

# 连接数据库服务器
client = pymongo.MongoClient('localhost', 27017)


db = client[db_name]
db.drop_collection(col_name)

# 关闭连接
client.close()
