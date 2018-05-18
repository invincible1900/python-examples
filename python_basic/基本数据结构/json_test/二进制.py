# coding:utf-8
# 验证json字符串不能表达二进制数据
# TypeError: Object of type 'bytes' is not JSON serializable

import json
import chardet
with open('equal_test.py', 'rb') as f:
    data = f.read()

print(type(data))
print(chardet.detect(data))

# a = {'bool': True, 'int': 1, 'bin': data}
# TypeError: Object of type 'bytes' is not JSON serializable

a = {'bool': True, 'int': 1, 'bin': data.decode('gbk')}
jstr = json.dumps(a, indent=2)
print(jstr)

jdata = json.loads(jstr)
print(jdata)

