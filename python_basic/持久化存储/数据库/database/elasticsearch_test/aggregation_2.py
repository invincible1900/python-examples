# coding:utf-8
# 获取指定字段不同值的总数

from elasticsearch import Elasticsearch
import json
es = Elasticsearch()

_index = 'indexname'   #修改为索引名
_type = 'typename'     #修改为类型名

# 聚合操作被置于顶层参数 aggs 之下（如果你愿意，完整形式 aggregations 同样有效）。
# 可能会注意到我们将 size 设置成 0 。我们并不关心搜索结果的具体内容，所以将返回记录数设置为 0 来提高查询速度
# body = {
#     "size" : 0,
#     "aggs" : {
#         "port_range" : {
#             "terms" : {
#               "field" : "port"
#             }
#         }
#     }
# }

# body = {"size":0,"aggregations":{"title_range":{"terms":{"field":"full_title"}}}}
# body = {"size":0,"aggregations":{"server_range":{"terms":{"field":"headers.server.keyword"}}}}
body = {"size":0,"aggregations":{"server_range":{"terms":{"field":"headers.content-type.keyword"}}}}
#
res = es.search(index=_index, doc_type=_type, body=body)

print(json.dumps(res, indent=2))