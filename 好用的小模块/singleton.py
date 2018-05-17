# coding:utf-8
# 实现 python 中的单例
# 原理：
# 利用函数包装器
from functools import wraps


def singleton(cls):
    instances = {}

    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance

# 以下为测试代码：

@singleton
class TClass1:
    def __init__(self):
        print("class1 created.")

class TClass2:
    def __init__(self):
        print("class2 created.")

if __name__ == '__main__':
    a = TClass1()
    b = TClass1()
    print(a == b)

    c = TClass2()
    d = TClass2()
    print(c == d)