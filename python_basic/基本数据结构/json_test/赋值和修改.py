# coding:utf-8
"""
使用copy
避免指针变量的修改导致原变量的值被修改

"""
a ={'data':  {'level': 1, 'url': 'www'}}
b = a['data']
print('*' * 100)
print('a:', a)
print('b:', b)
print('*' * 100)

b['level'] = 2
print('a:', a, '\t!!!!')
print('b:', b)
print('*' * 100)

c = a['data'].copy()
c['level'] = 3
print('a:', a)
print('c:', c)
print('*' * 100)

