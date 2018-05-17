# coding:utf-8
import pymongo
import json
import glob
from mytimer import MyTimer


db_name = 'dbname'
col_name = 'collectionname'

# 连接数据库服务器
client = pymongo.MongoClient('localhost', 27017)

db = client[db_name]
c = db[col_name]

err_files = {'files': []}
counter = 0
success = 0
failed = 0

# data也可以是一个字典列表
# json文件内容： { 'data': [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}, ...]}
with MyTimer() as timer:
    fnames = glob.glob(r'*.json')
    for fname in fnames:
        # print(fname)
        with open(fname, 'r') as f:
            try:
                data = json.loads(f.read())['data']
            except Exception as e:
                print(fname, e)
                err_files['files'].append({'fname': fname, 'error': str(e)})
                failed += 1
                continue

        # 插入数据
        try:
            c.insert(data)
            counter += len(data)
            success += 1
        except Exception as e:
            print(fname, e)
            err_files['files'].append({'fname': fname, 'error': str(e)})
            failed += 1
        print(u'成功导入%d个文件，失败%d个文件，共%d条数据，剩余%d个文件' % (success, failed, counter, len(fnames) - success - failed))
print(u'入库完成，共%d条数据，用时%ss' % (counter, str(timer.total)[:5]))

with open('error_files.json', 'w') as f:
    f.write(json.dumps(err_files, indent=2))

# 关闭连接
client.close()

