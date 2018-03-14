# coding:utf-8
import pymongo

# db_name = 'all_scan_result'
db_name = 'auth_net_device'
# db_name = 'live_net_device'
col_name = 'JP'

# 连接数据库服务器
client = pymongo.MongoClient('localhost', 27017)

db = client[db_name]
c = db[col_name]

# 查询所有数据
for i in c.find({}, {'_id': False}):
    print(i)
# r = list(c.find({}, {'_id': False}))
# for i in r[-1000:]:
#     print(i)

# print([i for i in c.find({'ip': '150.1.19.2253'}, {'_id': False})])

# 关闭连接
client.close()
