# coding:utf-8
"""
集合并差补交操作
"""

a = {1, 2, 5, 7}
b = {1, 2, 6, 8}

print('a: ', a)
print('b: ', b)
print()

# 求差集
print(u'差集 a - b:', a - b)
print(u'差集 a - b:', a.difference(b))
print(u'差集 b - a:', b - a)
print(u'差集 b - a:', b.difference(a))
print()

# 求交集
print(u'交集:', a & b)

# 求补集
print(u'补集:', (a - b) | (b - a))
print()

# 求并集
print(u'并集:', a | b)

# 求并集并修改
a.update(b)
print(u'并集:', a)