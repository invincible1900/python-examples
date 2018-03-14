# coding:utf-8
import pymongo

db_name = 'live_net_device'
client = pymongo.MongoClient('localhost', 27017)        #连接数据库服务器
client.drop_database(db_name)                           #删除数据库
client.close()                                          #关闭连接