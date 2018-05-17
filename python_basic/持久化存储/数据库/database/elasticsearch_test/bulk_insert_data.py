# coding:utf-8
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

_index = 'indexname'   #修改为索引名
_type = 'typename'     #修改为类型名

_index_settings = {
  "mappings": {
    _type: {
      "properties": {

      }
    }
  }
}

es = Elasticsearch()
if es.indices.exists(index=_index) is not True:
    es.indices.create(index = _index, body = _index_settings)

count = 0
doc = {}


data = [{'doc1': ''}, {'doc2': ''}, {'doc3': ''}]
actions = []
for doc in data:
    action = {
        "_index": _index,
        "_type": _type,
        "_source": doc
    }
    actions.append(action)

success, _ = bulk(es, actions, index = _index)
