# coding:utf-8
import hashlib
import time


def get_time_fp():
    m = hashlib.md5()
    data = str(time.time())
    m.update(data)
    fp = m.hexdigest()
    # print fp, len(fp)
    return fp


def get_data_fp(data):
    if not (isinstance(data, str) or isinstance(data, bytes)):
        data = str(data)

    m = hashlib.md5()
    m.update(data)
    fp = m.hexdigest()
    return fp

# get_time_fp()
# time.sleep(0.1)
# get_time_fp()
#
# a = get_data_fp(123)
# b = get_data_fp(123)
# print a == b
# b = get_data_fp(456)


