# coding:utf-8
# 操作redis的list
#
#                 _._
#            _.-``__ ''-._
#       _.-``    `.  `_.  ''-._
#   .-`` .-```.  ```\/    _.,_ ''-._
#  (    '      ,       .-`  | `,    )
#  |`-._`-...-` __...-.``-._|'` _.-'|
#  |    `-._   `._    /     _.-'    |
#   `-._    `-._  `-./  _.-'    _.-'
#  |`-._`-._    `-.__.-'    _.-'_.-'|
#  |    `-._`-._        _.-'_.-'    |
#   `-._    `-._`-.__.-'_.-'    _.-'
#  |`-._`-._    `-.__.-'    _.-'_.-'|
#  |    `-._`-._        _.-'_.-'    |
#   `-._    `-._`-.__.-'_.-'    _.-'
#       `-._    `-.__.-'    _.-'
#           `-._        _.-'
#               `-.__.-'


import redis


# 连接redis
r = redis.Redis(host='127.0.0.1', port=6379)
hash_name = 'hash name'

def create_hash(name, conn, data):
    """
    创建一个hash表,如已经存在则删除
    :param name: 表名
    :param conn: redis连接对象
    :param data: dict 类型数据
    :return:
    """
    if conn.exists(name):
        d = ''
        while not d.strip():
            d = input(u'%s已经存在，是否删除?(y/n): ' % name)
        if d.lower() == 'y':
            conn.delete(name)
            print(u'%s 已删除' % name)
        else:
            return
    conn.hmset(name, data)

def get_hash_table(name, conn):
    """
    获取hash表
    :return: dict 表对象,key-value都为字符串
    """
    res = conn.hgetall(name)
    ret = {}
    for k in res.keys():
        k = k.decode('utf-8')
        ret[k] = conn.hget(name, k).decode('utf-8')

    return ret

def get_key_value(name, conn, key):
    """
    获取指定key对应的值
    :return: bytes 类型的值
    """
    return conn.hget(name, key)

def change_value(name, conn, key, value):
    conn.hset(name, key, value)


if __name__ == '__main__':
    import json
    t = get_hash_table(hash_name, r)
    print(json.dumps(t, indent=2))
