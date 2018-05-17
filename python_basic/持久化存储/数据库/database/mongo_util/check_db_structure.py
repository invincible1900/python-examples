# coding:utf-8
import pymongo

client = pymongo.MongoClient('localhost', 27017)     # 连接数据库服务器

def show_db_status():
    dbnames = client.database_names()
    print(u'共有%d个数据库:' % len(dbnames))

    for dbname in dbnames:
        print(dbname + ':')
        db = client[dbname]
        colnames = db.collection_names()
        for colname in colnames:
            print('\tcollection: ' + colname, 'size:', db[colname].count({}))
        print()

show_db_status()

client.close()     # 关闭连接
