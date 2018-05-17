# coding:utf-8
# 操作redis的list
import redis

# 连接redis
r = redis.Redis(host='192.168.1.7', port=6379)
list_name = 'list name'

def get_list_size(name, conn):
    """
    获取列表大小
    :param name: 列表名称
    :param conn: redis连接对象
    :return: int 列表大小
    """
    return conn.llen(name)

def get_all_list_data(name, conn):
    """
    获取列表中的所有数据
    :return: 数据列表
    """
    size = conn.llen(name)
    return conn.lrange(name, 0, size-1)

def get_data_by_index(name, conn, index):
    """
    获取索引处的值
    :param name: 列表名
    :param conn: redis连接对象
    :param index: int 索引值
    :return: bytes 索引处的数据
    """
    return conn.lindex(name, index)

def add_to_list(name, conn, value):
    """
    向列表首部添加数据
    :return:
    """
    conn.lpush(name, value)

# def delete_by_index(name, conn, index):
#     """
#     :param name: 列表名
#     :param conn: redis连接对象
#     :param index: 索引值
#     :return:
#     无法实现
#     """
#     pass

# def delete_by_value(name, conn, value):
#     """
#     删除列表中所有值为value的项
#     :param name: 列表名
#     :param conn: redis连接对象
#     :param value: 删除的值
#     :return:
#     无法实现
#     """
#     pass
#
# def delete_by_contain_value(name, conn, value):
#     """
#     删除列表中包含value的项
#     :param name: 列表名
#     :param conn: redis连接对象
#     :param value: 包含的值
#     :return:
#     无法实现
#     """
#     pass

def delete_first(name, conn):
    """
    删除第一个元素
    :return:第一个元素的值
    """
    return conn.lpop(name)

def delete_last(name, conn):
    """
    删除第一个元素
    :return:第一个元素的值
    """
    return conn.rpop(name)





