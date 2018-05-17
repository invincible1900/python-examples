# coding:utf-8
"""
高亮搜索
"""

from elasticsearch import Elasticsearch
import json
_index = 'indexname'   #修改为索引名
_type = 'typename'     #修改为类型名

es = Elasticsearch()

body = {
    "query" : {
        "match_phrase" : {
            "html" : u"王者荣耀"
        }
    },
    "highlight": {
        "fields" : {
            "html" : {}
        }
    }
}

res = es.search(index=_index, doc_type=_type, body=body)

print(json.dumps(res, indent=2)[:4096])
with open('tmp.json', 'w') as f:
    f.write(json.dumps(res, indent=2))