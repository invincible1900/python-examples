# coding:utf-8
import os
import time
from python_basic.io_test import fingerprint
import json

def add(fmtdata):
    # 写入数据
    with open('test.txt', 'a') as f:
        f.write(fmtdata)

if __name__ == '__main__':
    t0 = time.time()
    with open('tem.txt', 'r')  as f:
        urls = f.readlines()
    # url_dics = [eval(i.strip()) for i in urls[:600000]]
    urls_str = [i.strip().replace("'",'"') for i in urls[:600000]]
    t1 = time.time()
    print('read %d datas ,use %ds' % (600000, (t1 - t0)))


    t0 = time.time()
    memcache = dict()
    counter = 0
    for u in urls:
        dic_u = eval(u)
        jstr = json.dumps(dic_u)
        urlid = '{}_{}'.format(dic_u.get('url'), str(dic_u.get('max_redirect')))
        hashid = fingerprint.get_data_fp(urlid.encode('utf-8'))
        if hashid in memcache.keys():
            counter += 1
            # print(hashid, jstr)

        memcache[hashid] = jstr

    t1 = time.time()
    print('read %d datas ,use %ds' % (600000, (t1 - t0)))


    print(len(memcache),'dup urls %d ' % counter)
    print(memcache.get('bdee33e002198dc0c13cd4d779f32124'))



