# coding:utf-8
import pymongo

db_name = 'ttt'
col_name = 'tt'

# 连接数据库服务器
client = pymongo.MongoClient('localhost', 27017)

db = client[db_name]
c = db[col_name]


# filter: A query that matches the document to delete.
key = 'key1'
value = 'value1'
filter = {key: value}

c.delete_one(filter=filter)


# 关闭连接
client.close()

