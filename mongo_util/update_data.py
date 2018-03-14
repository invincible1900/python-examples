# coding:utf-8
import pymongo

db_name = 'ttt'
col_name = 'tt'

# 连接数据库服务器
client = pymongo.MongoClient('localhost', 27017)

db = client[db_name]
c = db[col_name]

# A query that matches the document to update.
key = 'key1'
value = 'value1'
filter = {key: value}

# update: The modifications to apply.
key = 'key2'
value = 'up_value2'
update = {'$set': {key: value}}

# upsert (optional): If True, perform an insert if no documents match the filter.
upsert = False

# 插入数据
c.update_one(filter=filter, update=update, upsert=upsert)

# 关闭连接
client.close()

