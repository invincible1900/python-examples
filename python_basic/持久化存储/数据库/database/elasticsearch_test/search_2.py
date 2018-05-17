# coding:utf-8
"""
对nested对象查询
多字段查询
参考：https://www.elastic.co/guide/cn/elasticsearch/guide/current/multi-match-query.html

"""
from elasticsearch import Elasticsearch
import json
_index = 'indexname'   #修改为索引名
_type = 'typename'     #修改为类型名

es = Elasticsearch()

mapping = es.indices.get_mapping(index=_index)
print(json.dumps(mapping, indent=2))

# match 查询
# body = {
#     "_source": ["title", "ip", "headers"],
#     "query":{
#         "match":{
#             "full_server": "nginx/1.9.7"       # 有结果
#             # "headers": "server"   # 无结果
#             # "headers": "nginx"    # 无结果
#             # "headers.server": "nginx/1.9.7"   # 无结果
#             # "headers.server": "nginx"   # 无结果
#             # "full_server": "nginx"            # 无结果
#         }
#     }
# }

# term 查询
# body = {
#     "query" : {
#         "constant_score" : {
#             "filter" : {
#                 "term" : {
#                     "full_server": 'nginx/1.9.7'
#                 }
#             }
#         }
#     }
# }

# 对nested类型的headers的server字段查询
# 因嵌套对象(nested objects)会被索引为分离的隐藏文档，我们不能直接查询它们。而是使用 nested查询或 nested 过滤器来存取它们

# body = {
#     "query" : {
#         "nested" : {
#             "path" : "headers",
#             "query" : {
#                  "match": { "headers.server": "nginx" },
#             }
#         }
#     }
# }

# nested类型的headers所有字段查询
# body = {
#     "query" : {
#         "nested" : {
#             "path" : "headers",
#             "query" : {
#                 "multi_match": {
#                     "query":  "text",
#                     "fields": [ "headers.*"]
#                 }
#             }
#         }
#     }
# }

# objec类型的headers查询方法
body = {
    "_source": ["title", "ip", "headers"],
    "query" : {
        "multi_match": {
            "query":  "php",
            "fields": [ "headers.*"]
        }
    }
}

res = es.search(index=_index, doc_type=_type, body=body)

print(json.dumps(res, indent=2)[:1024])
with open('tmp.json', 'w') as f:
    f.write(json.dumps(res, indent=2))