# coding:utf-8
"""
删除文档

"""
from elasticsearch import Elasticsearch

_index = 'xx'   #修改为索引名
_type = 'xx'     #修改为类型名
_id = 'xx'      # 修改为文档ID

es = Elasticsearch()
es.delete(_index, _type, id=_id)