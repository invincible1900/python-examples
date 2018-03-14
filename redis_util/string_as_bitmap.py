# coding:utf-8
# 操作redis的string
import redis

# 连接redis
r = redis.Redis(host='192.168.1.7', port=6379)
str_name = 'test_string'