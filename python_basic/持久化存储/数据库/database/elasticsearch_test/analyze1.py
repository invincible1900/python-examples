# coding:utf-8
# GET /my_store/_analyze

from elasticsearch import Elasticsearch
import json
_index = 'indexname'   #修改为索引名
_type = 'typename'     #修改为类型名

es = Elasticsearch()

body = {
  "field": "headers",
  "text": "nginx/1.9.7"
}

res = es.indices.analyze(index=_index, body=body)
print(json.dumps(res, indent=2))
