# coding:utf-8
# 获取doc总数的总字节数

from elasticsearch import Elasticsearch

es = Elasticsearch()
print(es.cat.count(index='indexname'))
