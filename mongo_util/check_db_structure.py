# coding:utf-8
import pymongo

client = pymongo.MongoClient('localhost', 27017)     # 连接数据库服务器


def show_db_status():
    print('\ndb names:')
    dbs = client.database_names()
    for db in dbs:
        print('\t' + db)

    print('\ncollections:')
    for db in dbs:
        db = client[db]
        cols = db.collection_names()
        for col in cols:
            print('\tname:' + db.name + '.' + col)
            print('\tsize:', db[col].count({}))
            print()

show_db_status()

client.close()     # 关闭连接
