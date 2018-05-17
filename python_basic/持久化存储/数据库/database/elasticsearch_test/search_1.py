# coding:utf-8
"""
查询所有
"""
from elasticsearch import Elasticsearch
import json
_index = 'indexname'   #修改为索引名
_type = 'typename'     #修改为类型名

es = Elasticsearch()

# 搜索所有数据
# res = es.search(index=_index,doc_type=_type)

# 或者
body = {
    "_source": ["title", "ip", "headers"],
    "query":{
        "match_all":{}
    }
}
res = es.search(index=_index, doc_type=_type, body=body)

print(json.dumps(res, indent=2))