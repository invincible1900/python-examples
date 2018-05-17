# coding:utf-8
# 使用string的setnx作为事务锁
# setnx: 只有在 key 不存在时设置 key 的值

import redis


# 连接redis
r = redis.Redis(host='192.168.1.7', port=6379)
lock_name = 'test_lock'

def get_lock(name, conn):
    """
    获取资源锁
    :param name: 锁名称
    :param conn: redis连接对象
    :return:
    """
    while not conn.setnx(name, 'lock test'):
        pass
    conn.expire(name, 20)

def release_lock(name, conn):
    """
    释放锁
    :param name: 锁名称
    :param conn: redis连接对象
    :return:
    """
    conn.delete(name)


def main():
    import time
    get_lock(lock_name, r)
    print('proc got lock')
    # 做多个操作：
    # 查表，修改表等
    # 由于锁的存在，多个操作被封装成一个事务，不会被中断
    time.sleep(10)
    release_lock(lock_name, r)
    print('proc release lock after 10 s')


if __name__ == '__main__':
    main()
