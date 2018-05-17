# coding:utf-8
import json


a = {'a': '中文'}
json_a = json.dumps(a).encode('utf-8').decode('utf-8')
for i in json_a:
    print(i)
    # print ord(i), i
    # print(type(ord(i) ^ 56))

# print(135 ^ 65)
# print(ord('6'))
# print(chr(60))

print(type(u'中文'))
for i in u'中文':
    print(i)

print(type(u'中文'.encode('utf-8')))
for i in u'中文'.encode('utf-8'):
    print(i)

print(type(a['a'].decode('utf-8')))
for i in a['a'].decode('utf-8'):
    print(i)