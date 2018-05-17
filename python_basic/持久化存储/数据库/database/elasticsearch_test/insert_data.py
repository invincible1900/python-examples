# coding:utf-8
from elasticsearch import Elasticsearch

_index = 'indexname'   #修改为索引名
_type = 'typename'     #修改为类型名
es = Elasticsearch()

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
                    },
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
if es.indices.exists(index=_index) is not True:
    es.indices.create(index=_index, body=_index_mappings)


doc = {
	"url": "http://112.121.74.210:80",
	"title": "蟻力股份有限公司 | Ants' Power Company Limited",
	"headers": {
		"server": "nginx/1.9.7",
		"content-type": "text/html; charset=UTF-8",
		"transfer-encoding": "chunked",
		"connection": "keep-alive",
		"x-powered-by": "PHP/5.3.3",
		"link": "<http://www.antspw.com/cht/wp-json/>; rel=\"https://api.w.org/\"",
		"content-encoding": "gzip",
        "date": "2014-01-01"
	},
	"html": "<!DOCTYPE html>\r\n<html lang=\"zh-TW\">\r\n<head>\r\n<titlet});\r\n</script>\r\n</body>\r\n</html>",
	"res_code": 200,
	"time": "2018-05-04 13:47:47",
	"ip": "112.121.74.210",
	"port": 80
}
es.index(index=_index, doc_type=_type, body=doc)
