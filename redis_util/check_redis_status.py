import redis

# 连接redis
r = redis.Redis(host='192.168.1.7', port=6379)

print(u'当前数据库的 key 的数量:',r.dbsize())

print(u'当前redis中的所有key以及类型和大小:')
for k in r.keys():
    k_name = k.decode('utf-8')
    k_type = r.type(k).decode('utf-8')
    if k_type == 'list':
        k_size = r.llen(k)
    elif k_type == 'set':
        k_size = r.scard(k)
    elif k_type == 'string':
        k_size = r.strlen(k)
    elif k_type == 'hash':
        k_size = r.hlen(k)
    else:
        k_size = 0

    print()
    print(u'名称:', k_name)
    print(u'类型:', k_type)
    print(u'大小:', k_size)
    print()