# coding:utf-8
import redis

key = 'lock'
# 连接redis
r = redis.Redis(host='127.0.0.1', port=6379)

r.delete(key)