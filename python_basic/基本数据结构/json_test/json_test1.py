# coding:utf-8
"""
dict 转成 str 会保留双引号，不是标准的json字符串，json.loads会报错
要获得标准json字符串就用json.dumps()
"""
import json
# f = open('test.txt','w')

ddata = {'url': 'http://www.moj.gov.cn/', 'level': 3, 'max_redirect': 2, 'cn': '中文', 'ucn': u'中文'}
sdata = str(ddata)
jddata = json.dumps(ddata)
jldata = json.loads(jddata)


try:
    jlsdata = json.loads(sdata)
except Exception as e:
    print(e)



print(type(sdata), sdata)
print(type(ddata), ddata)
print(type(jddata), jddata)
print(type(jldata), jldata)
