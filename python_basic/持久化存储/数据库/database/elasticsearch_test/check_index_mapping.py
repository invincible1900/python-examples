from elasticsearch import Elasticsearch
import json


_index = '_indexname'
es = Elasticsearch()
mapping = es.indices.get_settings(index=_index)
print(json.dumps(mapping, indent=2))

mapping = es.indices.get_mapping(index=_index)
print(json.dumps(mapping, indent=2))



