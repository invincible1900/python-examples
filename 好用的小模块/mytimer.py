# coding:utf-8
import time
class MyTimer(object):
    """
    利用上下文管理器封装的一个对代码块执行时间计时器

    """

    def __init__(self):
        self.start = 0
        self.end = 0
        self.total = 0

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.total = self.end - self.start