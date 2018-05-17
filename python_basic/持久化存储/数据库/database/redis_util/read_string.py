# coding:utf-8
"""
读字符串内容

"""
import redis
names = ['stringname1', 'stringname2']

r = redis.Redis(host='127.0.0.1', port=6379)
for name in names:
    s = r.get(name)
    print(s)