# coding:utf-8
import pymongo

db_name = 'net_device'
col_name = 'TW'

# 连接数据库服务器
client = pymongo.MongoClient('localhost', 27017)

db = client[db_name]
c = db[col_name]

# data也可以是一个字典列表
data = {'ip': '61.30.201.89', 'port': 80, 'password': '123456', 'username': 'admin'}

# 插入数据
c.insert(data)

# 关闭连接
client.close()

