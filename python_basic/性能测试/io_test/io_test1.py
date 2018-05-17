# coding:utf-8
import os
import time
from python_basic.io_test import fingerprint
import json


# 查询
def get(hashid):
    t0 = time.time()
    with open('test.txt', 'r') as f:
        file_dic = json.loads(f.read())
    t1 = time.time()
    print(file_dic.get(hashid),'get one data, use %ds' % (t1-t0))


# 添加数据
def add(hashid, ddata):
    t0 = time.time()
    if os.path.exists('test.txt'):
        with open('test.txt', 'r') as f:
            file_dic = json.loads(f.read())
            file_dic[hashid] = json.dumps(ddata)

    else:
        file_dic = {hashid: json.dumps(ddata)}

    # 写入数据
    with open('test.txt', 'w') as f:
        f.write(json.dumps(file_dic))
    t1 = time.time()
    # print('add one data ,use %ds' % (t1-t0))

# 添加多条数据
def add_datas(datas):
    t0 = time.time()

    with open('test.txt', 'r') as f:
        file_dic = json.loads(f.read())

    for d in datas:
        file_dic[d[0]] = d[1]

    # 写入数据
    with open('test.txt', 'w') as f:
        f.write(json.dumps(file_dic))

    t1 = time.time()

    print('add %d datas ,use %ds' % (len(datas), (t1-t0)))


if __name__ == '__main__':
    # with open('test.txt', 'r') as f:
    #     file_dic = json.loads(f.read())

    # ddata = {'url': 'http://www.moj.gov.cn/', 'level': 3, 'max_redirect': 2}
    # urlid ='{}_{}'.format(ddata.get('url'), ddata.get('max_redirect'))
    # hashid = fingerprint.get_data_fp(urlid.encode('utf-8'))
    # file_dic = {hashid: ddata}
    # print(file_dic)
    # t0 = time.time()

    # with open('tem.txt','r')  as f:
    #     url_dics = [eval(i.strip()) for i in f.readlines()[:10000]]
    #
    # t1 = time.time()
    # print('read %d datas ,use %ds' % (10000, (t1-t0)))
    #
    #
    # t0 = time.time()
    # for ddata in url_dics[:10000]:
    #     urlid ='{}_{}'.format(ddata.get('url'), ddata.get('max_redirect'))
    #     hashid = fingerprint.get_data_fp(urlid.encode('utf-8'))
    #     add(hashid, ddata)

    # t1 = time.time()
    # print('add %d datas ,use %ds' % (10000, (t1-t0)))
    get('e1d8d54dd462d66dde81cadba9acdd17')


