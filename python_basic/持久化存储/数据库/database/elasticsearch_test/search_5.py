# coding:utf-8
from elasticsearch import Elasticsearch
import json
"""
exist查询

指定字段查询

"""
_index = 'indexname'   #修改为索引名
_type = 'typename'     #修改为类型名

es = Elasticsearch()

body = {
    "_source": ["title", "ip", "headers"],
    "query" : {
        "constant_score" : {
            "filter" : {
                "exists" : { "field" : "headers.date" }
            }
        }
    }
}


res = es.search(index=_index, doc_type=_type, body=body)

print(json.dumps(res, indent=2)[:2048])
with open('tmp.json', 'w') as f:
    f.write(json.dumps(res, indent=2))