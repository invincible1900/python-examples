from elasticsearch import Elasticsearch

es = Elasticsearch()
print(es.cat.indices())
