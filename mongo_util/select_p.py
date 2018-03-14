# coding:utf-8
import pymongo

db_name = 'all_scan_result'
# db_name = 'auth_net_device'
# db_name = 'live_net_device'
col_name = 'JP'

# 连接数据库服务器
client = pymongo.MongoClient('localhost', 27017)

db = client[db_name]
c = db[col_name]
print(c.count())
# 查询所有数据
# print('\n'.join([str(i) for i in c.find({"$or": [{'ip': '150.1.0.1'}, {'ip': '150.1.0.2'}]}, {'_id': False})]))
print('\n'.join([str(i) for i in c.find({"$or": [{'ip': '126.3.65.8'}, {'ip': '150.2.4.115'}]}, {'_id': False})]))


def select_one(target):
    return [i for i in c.find(target, {'_id': False})]


def ip_scanned(ip):
    res = select_one({'ip': ip})
    if not res:
        return False
    else:
        for i in res:
            print(i)
        return True

print(ip_scanned('45.34.157.232'))
# 关闭连接
client.close()
