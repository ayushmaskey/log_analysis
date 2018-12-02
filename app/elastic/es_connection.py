from elasticsearch import Elasticsearch

def es_connect():
	"""Connects to elastic on localhost and returns client object
	
	Usage:
	>>> es_client = Elasticsearch(['http://localhost:9200/'], verify_certs=True)
	>>> type(es_client)
	<class 'elasticsearch.client.Elasticsearch'>
	>>> es_client
	<Elasticsearch([{'host': 'localhost', 'port': 9200}])>

	"""
	es_client = Elasticsearch(['http://localhost:9200/'], verify_certs=True, timeout=30)
	if not es_client.ping():
	    raise ValueError("Connection failed")
	return es_client



if __name__ == "__main__":
	import doctest
	doctest.testmod()
	help(es_connect)
