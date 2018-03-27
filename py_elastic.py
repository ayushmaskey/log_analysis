from elasticsearch import Elasticsearch
from request_json import sample_json1

#connection to elastic_py
def elastic_connection_py():
	'''connects to elastic on localhost and returns client'''
	es = Elasticsearch(['http://localhost:9200/'], verify_certs=True)
	if not es.ping():
	    raise ValueError("Connection failed")
	return es

def print_response_layer(res):
	'''takes search as input
	returns aggregates
	'''
	for r in res['aggregations']:
		print(r)


if __name__ == "__main__":
	client = elastic_connection_py()
	query = sample_json1()
	result= client.search(index="*", body=query)	

	print(result)
	#print_response_layer(result)
