
from elasticsearch import Elasticsearch

def es_connect():
	""" connects to elastic on localhost and returns client object
	
	>>> es_client = Elasticsearch(['http://localhost:9200/'], verify_certs=True)
	>>> es_client
	<Elasticsearch([{'host': 'localhost', 'port': 9200}])>

	"""
	es_client = Elasticsearch(['http://localhost:9200/'], verify_certs=True)
	if not es_client.ping():
	    raise ValueError("Connection failed")
	return es_client


