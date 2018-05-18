# coding:utf-8
"""
二维列表转一维列表的方法
"""
a = [[1,2], [3,4], ['a', 'b']]
print(sum(a, []))

a = [[1,2], [3,4], ['abc', 'b'], [['c', 'd'], ['e', 'f']]]
print(sum(a, []))

try:
    print(sum(sum(a, []), []))
except Exception as e:
    print(e)