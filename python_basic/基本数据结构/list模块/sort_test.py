# coding:utf-8
"""
sort,reverse()函数不会返回值，直接修改调用的对象

"""

a = {'1': 'a', '5': 'b', '3': 'c'}

keys = [int(k) for k in a.keys()]
print('print(keys) : ', keys)
print('print(keys.sort()):', keys.sort())
print('keys.reverse():', keys.reverse())
print('print(keys):', keys)

for k in keys:
  k = str(k)
  print(k, a[k])
