
from elasticsearch import Elasticsearch

def es_connect():
	'''connects to elastic on localhost and returns client'''
	es_client = Elasticsearch(['http://localhost:9200/'], verify_certs=True)
	if not es_client.ping():
	    raise ValueError("Connection failed")
	return es_client


def db_connect():
	db_client = 'some database'
	return db_client

if __name__ == "__main__":
	es = es_connect()
	print(es)