# coding:utf-8
"""
短语查询
"""
from elasticsearch import Elasticsearch
import json
_index = 'indexname'   #修改为索引名
_type = 'typename'     #修改为类型名

es = Elasticsearch()

body = {
    "query": {
        "match_phrase": { "html": u"key1 key2 key3" }
    }
}

res = es.search(index=_index, doc_type=_type, body=body)

print(json.dumps(res, indent=2)[:2048])
with open('tmp.json', 'w') as f:
    f.write(json.dumps(res, indent=2))