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
r = redis.Redis(host='192.168.1.7', port=6379)
hash_name = 'scan_map'

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

def main1():
    import json
    import struct
    import socket
    from collections import OrderedDict

    def ip_str_to_in(_ip):
        """
        将字符串IP地址转换成int形式
        :param _ip: 字符串类型的点分十进制IP地址
        :return: int类型的IP地址
        """
        return struct.unpack('!I', socket.inet_aton(_ip))[0]

    res = get_hash_table(hash_name, r)

    sorted_res = OrderedDict()

    for k in sorted(res.keys(), key=lambda x: ip_str_to_in(x), reverse=False):
        sorted_res[k] = res[k]

    with open('tmp.txt', 'w') as f:
        f.write(json.dumps(sorted_res, indent=2))

def main2():
    print(get_key_value(hash_name, r, '1.1.0.0').decode('utf-8'))

def main3():
    change_value(hash_name, r, '1.1.0.0', 3)

def main4():
    create_hash(hash_name, r, {'1':'a'})

def main5():
    import json
    print(json.dumps(get_hash_table(hash_name, r), indent=2))

if __name__ == '__main__':
    main1()