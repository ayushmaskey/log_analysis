
def es_connect():
	'''connects to elastic on localhost and returns client'''
	es_client = Elasticsearch(['http://localhost:9200/'], verify_certs=True)
	if not es_client.ping():
	    raise ValueError("Connection failed")
	return es_client


def db_connect():
	return db_client