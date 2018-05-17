# coding:utf-8
from elasticsearch import Elasticsearch

_index = 'indexname'   #修改为索引名
_type = 'typename'     #修改为类型名

es = Elasticsearch()

es.indices.put_settings(body={"settings": {
            "index.mapping.total_fields.limit": 5000
         }}, index=_index)

