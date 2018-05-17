# coding:utf-8
# 更新index的mapping
# 不能修改

from elasticsearch import Elasticsearch

_index = 'indexname'   #修改为索引名
_type = 'typename'     #修改为类型名


es = Elasticsearch()

body = {
    "date_detection": False,
    "properties": {
        "headers":{
            "properties": {
                "date": {
                    "type": "text"
                }
            }
        }
    }
}

es.indices.put_mapping( index=_index, doc_type=_type, body=body)


# coding:utf-8
# 查看index的settings
from elasticsearch import Elasticsearch
import json

es = Elasticsearch()
mapping = es.indices.get_mapping(index=_index)
print(json.dumps(mapping, indent=2))
