# coding:utf-8
import pymongo
import re
from mytimer import MyTimer

db_name = 'dbname'
col_name = 'collectionname'

# 连接数据库服务器
client = pymongo.MongoClient('localhost', 27017)

db = client[db_name]
c = db[col_name]
print(u'数据库[ %s ]集合[ %s ]共%d条数据' % (db_name, col_name, c.count()))


# 查询条件：所有html字段包含"Login"字符串的数据
with MyTimer() as timer:
    res = c.find({'title': re.compile('keyword')})
    res = list(res)

print(u'查询完成，html字段包含 "keyword" 字符串的数据有%d条，查询时间%ss' % (len(res), str(timer.total)[:5]))

for d in res[:10]:
    print(d)


# 关闭连接
client.close()
