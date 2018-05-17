# coding:utf-8
from elasticsearch import Elasticsearch
import json
_index = 'smartcn_test'   #修改为索引名
_type = 'ttt'     #修改为类型名

es = Elasticsearch()

_index_mappings = {
  "mappings": {
    _type: {
      "properties": {
        "html": {
          "type": "text",			# html需要分词
          "index": True,
          "analyzer": "smartcn"	 # 使用smartcn分词器
        }
      }
    }
  }
}

es.indices.create(index=_index, body=_index_mappings)

body = {
  "field": "html",
  "text": "我是中国人"
}

res = es.indices.analyze(index=_index, body=body)

print(json.dumps(res, indent=2))
