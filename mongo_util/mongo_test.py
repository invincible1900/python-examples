import pymongo

client = pymongo.MongoClient('localhost',27017)     #连接数据库服务器

print(client.database_names())     #列出所有数据库名称
#
db = client['camera']     #使用名称为pythondb的数据库
# db.name     #当前数据库名称
#
print(db.collection_names())     #获取数据库中的表名
# db.drop_collection('col_name')     #删除一个集合（Table）
# c = db.table_name 或 c = db['table_name']     #创建一个集合（表）：
c = db['motorblog']
# data = {'_id':num,'key1':'value1','key2':'value2'}     #data也可以是一个字典列表
# c.insert(data)      #插入数据
#
for i in c.find():
     print (i)     #查询所有数据
#
# c.find().sort('列名',-1）倒序排序

client.close()     #关闭连接

