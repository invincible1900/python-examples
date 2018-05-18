# coding:utf-8
import struct
import socket
import logging
LOGGER = logging.getLogger()


def ip_str_to_int(_ip):
    """
    将字符串IP地址转换成int形式
    :param _ip: 字符串类型的点分十进制IP地址
    :return: int类型的IP地址
    """
    return struct.unpack('!I', socket.inet_aton(_ip))[0]

rmap = {'1.1.0.0': 0, '1.0.0.0': 0, '110.11.0.0': 0}

# 按照key大小排序后保存到文件
from collections import OrderedDict
import json

order_map = OrderedDict()
order_keys = sorted(rmap.keys(), key=lambda x: ip_str_to_int(x), reverse=False)
for k in order_keys:
    order_map[k] = rmap[k]

print(json.dumps(order_map, indent=2))
