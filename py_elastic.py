from elasticsearch import Elasticsearch
from request_json import sample_json1

#connection to elastic_py
def elastic_connection_py():
	es = Elasticsearch(['http://localhost:9200/'], verify_certs=True)
	if not es.ping():
	    raise ValueError("Connection failed")
	return es


#####################################################################
if __name__ == "__main__":
	client = elastic_connection_py()
	query = sample_json1
'''	result= client.search(index="*", body=query)	

	for r in result:
		print(r)

	print()

	for f in result['aggregations']:
		print(f)

	print()

	for g in result['aggregations']['tag_name']:
		print(g)

	print()

	for h in result['aggregations']['tag_name']['buckets']:
		print(h)	
'''

