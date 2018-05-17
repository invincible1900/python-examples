# coding:utf-8
"""
加快查询速度的方法
"""
from elasticsearch import Elasticsearch
import json
_index = 'indexname'   #修改为索引名
_type = 'typename'     #修改为类型名

es = Elasticsearch()

# 1. term 查询通过不要评分加快
body = {
    "query" : {
        "constant_score" : {
            "filter" : {
                "term" : {
                    "headers.server": 'apache'
                }
            }
        }
    }
}


res = es.search(index=_index, doc_type=_type, body=body)

print(json.dumps(res, indent=2))

