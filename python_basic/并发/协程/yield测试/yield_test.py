# coding:utf-8
# def consumer():         # 定义消费者，由于有yeild关键词，此消费者为一个生成器
#     print("[Consumer] Init Consumer ......")
#     r = "init ok"       # 初始化返回结果，并在启动消费者时，返回给生产者
#     while True:
#         n = yield r     # 消费者通过yield接收生产者的消息，同时返给其结果
#         print("[Consumer] conusme n = %s, r = %s" % (n, r))
#         r = "consume %s OK" % n     # 消费者消费结果，下个循环返回给生产者
#
# def produce(c):         # 定义生产者，此时的 c 为一个生成器
#     print("[Producer] Init Producer ......")
#     r = c.send(None)    # 启动消费者生成器，同时第一次接收返回结果
#     print("[Producer] Start Consumer, return %s" % r)
#     n = 0
#     while n < 5:
#         n += 1
#         print("[Producer] While, Producing %s ......" % n)
#         r = c.send(n)   # 向消费者发送消息并准备接收结果。此时会切换到消费者执行
#         print("[Producer] Consumer return: %s" % r)
#     c.close()           # 关闭消费者生成器
#     print("[Producer] Close Producer ......")
#
# produce(consumer())
import requests
import time
# def consumer():
#     print "[Consumer] Init Consumer ......"
#     response = 'init ok'
#     while True:
#         url = yield response
#         # time.sleep(5)
#         response = '<html>xxxx</html>'
#
#
#
# def produce(c, urls):
#     print "[Producer] Init Producer ......"
#     response = c.send(None)
#     print("[Producer] Start Consumer, return %s" % response)
#     for url in urls:
#         print '[Producer] Send request for:%s' % url
#         response = c.send(url)
#         print '[Producer] Get response from url: %s(%d)' % (url, len(response))


#
# if __name__ == '__main__':
#     urls = [
#         'http://www.baidu.com',
#         'http://www.163.com',
#         'http://www.sina.com',
#         'http://www.google.com',
#         'http://www.sohu.com'
#     ]
#     produce(consumer(), urls)