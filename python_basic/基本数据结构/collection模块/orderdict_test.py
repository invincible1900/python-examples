# coding:utf-8
"""
OrderDict使用：
可以保证key的顺序按照数据插入的顺序保存
"""
from collections import OrderedDict
import json

d = OrderedDict()
d[3] = 3
d[1] = 1
d[2] = 2
print(json.dumps(d, indent=2))
