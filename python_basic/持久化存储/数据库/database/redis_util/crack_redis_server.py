# coding:utf-8
import redis
r = redis.Redis(host='127.0.0.1', port=6379)

# 获取目标配置目录
res = r.config_get('dir')
print(res)

# 获取目标dbfilename
res = r.config_get('dbfilename')
print(res)

# 设置config的dir参数1
res = r.config_set('dir', '.ssh/')
print(res)
res = r.config_get('dir')
print(res)


