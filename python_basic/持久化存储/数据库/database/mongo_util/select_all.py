# coding:utf-8
import pymongo
import json

db_name = 'dbname'
col_name = 'collectionname'
# 连接数据库服务器
client = pymongo.MongoClient('localhost', 27017)

db = client[db_name]
c = db[col_name]

res = {'data': []}
# 查询所有数据
for i in c.find({}, {'_id': False}):
    # print(type(i))
    res['data'].append(i)

# 数据保存到文件
with open(col_name + '.json', 'w') as f:
    f.write(json.dumps(res, indent=2))

# 关闭连接
client.close()
