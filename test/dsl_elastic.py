#from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections, Search, Q
from json_py_dsl import json_equivalent_from_dsl, dsl_equivalent_from_json
from request_json import total_traffic_count_30m_interval, sample_json2

from datetime import date, datetime
import pprint


#connection to elastic_dsl
def elastic_connection_dsl():
	'''
	creates a connection to elasticsearch
	can connect to more than one
	returns the connection object
	'''
	es = connections.create_connection( hosts= ['localhost'], timeout=20)
	return es

def total_docs_all_indices(search, str="total"):
	'''
	takes parameter search object
	return total documents in that search
	'''
	total = search.count()
	print(str, total)

def json_equivalent_from_dsl(c):
	'''
	convert query dsl to json query
	print json query
	return json object
	'''
	json = c.to_dict()
	print(json)
	return json

def dsl_equivalent_from_json(c):
	'''
	convert json query to query dsl
	print query dsl
	return dsl object
	'''
	d = Search.from_dict(c)
	dsl = d.query._proxied
	print(dsl)
	return dsl

#####################################################################
if __name__ == "__main__":
	client = elastic_connection_dsl()
	s = Search(using=client)

