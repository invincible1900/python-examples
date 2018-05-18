# coding:utf-8
"""
字符串的split，rsplit方法

"""
a = 'www.abc.com'
b = 'xxxx.txt'
c = '/user/bin/x.x.x.sh'

print(a.rsplit('.'))
print(a.rsplit('.', 1))

print(c.split('.', 1))