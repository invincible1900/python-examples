#coding: utf-8
import sys

a = '中文'
b = b'\xe4\xb8\xad\xe6\x96\x87'
c = b'\xd6\xd0\xce\xc4'
d = u'\u4e2d\u6587'
request = 'GET / HTTP/1.1\r\nHost: example.com\r\n\r\n'

print (sys.getdefaultencoding())
print ('a:',a)
print ('b.decode(utf-8):',b.decode('utf-8'))
print ('c.decode(gbk):',c.decode('gbk'))

print ('d:',d,type(d))

print ('a.encode(utf-8):',a.encode('utf-8'))
print ('a.encode(gbk):',a.encode('gbk'))

print ("request.encode('ascii'):",request.encode('ascii'))