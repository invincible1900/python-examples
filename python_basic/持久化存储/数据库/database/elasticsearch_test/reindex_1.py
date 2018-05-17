# coding:utf-8
# 更新index的mapping
from elasticsearch import Elasticsearch

_index = 'indexname'   #修改为索引名
_type = 'typename'     #修改为类型名
_new_index = 'new_' + _index

_index_mappings = {
  "mappings": {
    _type: {
      "date_detection": False,
      "properties": {

        "full_html": {
          "type": "keyword",		# 用于将html全文作为keyword保存
          "ignore_above": 1024,
        },
        "full_title": {
          "type": "keyword",		# 用于将title全文作为keyword保存
          "ignore_above": 1024,
        },
        "full_server": {
          "type": "keyword",		# 用于将headers.Server全文作为keyword保存
          "ignore_above": 1024,
        },
        "url": {
          "type": "keyword",
          "ignore_above": 1024,
        },
        "title": {
          "type": "text",               # title需要分词
          "index": True,		        # title需要分词
          "analyzer": "smartcn",        # 使用smartcn分词器
          "store": True,
          "copy_to": "full_title"       # 全文保存到full_title
        },
        "headers": {
            "type": "object",
            "properties": {
                "server":
                    {
                        "type": "text" ,		# headers.Server需要分词
                        "index": True,
                        "analyzer": "smartcn",	# 使用smartcn分词器
                        "store": True,
                        "copy_to": "full_server" # 全文保存到full_server
                    }
              }
        },
        "html": {
          "type": "text",			# html需要分词
          "index": True,
          "analyzer": "smartcn",	 # 使用smartcn分词器
          # "store": True,
          "copy_to": "full_html" 	 # 全文保存到full_server
        },
        "res_code": {
          "type": "integer"
        },
        "time": {
          "type": "keyword"
        },
        "ip": {
          "type": "keyword"
        },
        "port": {
          "type": "integer"
        }
      }
    }
  }
}


es = Elasticsearch()
if es.indices.exists(index=_new_index) is not True:
    es.indices.create(index=_new_index, body=_index_mappings)


body = {
  "source": {
    "index": _index
  },
  "dest": {
    "index": _new_index
  }
}
#
es.reindex(body)
#
#
# 查看index的settings
import json

es = Elasticsearch()
mapping = es.indices.get_mapping(index=_new_index)
print(json.dumps(mapping, indent=2))
