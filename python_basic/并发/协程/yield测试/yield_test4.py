# -*- coding: utf-8 -*-
"""
Topic: 协程
生产者-消费者实现
"""
import time
def consumer():
    print ('consumer')
    r = 'first'
    res = yield r
    print (res)
    print ('done')
    # while True:
    #     n = yield r
    #     if not n:
    #         yield 'return'
    #         print ('return ')
    #         return
    #     print('[CONSUMER] Consuming %s...' % n)
    #     time.sleep(1)
    #     r = '200 OK'


def producer(c):
    # print (next(c))
    print (c.send(None))
    print ('hey')
    n = 0
    while n < 5:
        n += 1
        # print('[PRODUCER] Producing %s...' % n)
        print ('send')
        try:
            r = c.send(n)
        except:
            print ('exception')
            break
        print ('sent')
        # print('[PRODUCER] Consumer return: %s' % r)
    print ('close')
    # c.close()
    # print (c.send(None))
    print ('closed')

if __name__ == '__main__':
    c = consumer()
    producer(c)