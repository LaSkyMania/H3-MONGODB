from elasticsearch import Elasticsearch
es = Elasticsearch('http://localhost:9200')

doc1 = {"text" : "Phrase du doc 1"}
response = es.index(index="french", id=1, body=doc1)

print(response)