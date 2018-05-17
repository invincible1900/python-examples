# coding:utf-8
# 创建db必须只是创建一个collection
import pymongo

db_name = 'dbname'
col_name = 'collectionname'

# 连接数据库服务器
client = pymongo.MongoClient('localhost', 27017)


db = client[db_name]
c = db.create_collection(col_name)

# 关闭连接
client.close()