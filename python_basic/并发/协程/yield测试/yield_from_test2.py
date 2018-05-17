# coding:utf-8
"""
yield和yield from的区别

"""
def f():
    yield from range(10)

def y():
    for i in range(10):
        yield i
        print (i)


l1 = (list(f()))
print (l1)

print('*' * 50)
l2 = (list(y()))
print (l2)

