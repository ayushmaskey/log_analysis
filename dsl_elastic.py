#from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections, Search, Q

from datetime import date, datetime
import pprint


#connection to elastic_py
def elastic_connection_py():
	es = Elasticsearch(['http://localhost:9200/'], verify_certs=True)
	if not es.ping():
	    raise ValueError("Connection failed")
	return es


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
	print()
	return dsl

#########################################################################################
def sample_json1():
	'''kibana 24hour json'''
	body = {
		"query": {
		 "bool": {
		  "must": [
		   {
		    "query_string": {
		     "query": "*",
		     "analyze_wildcard": "true"
		    }
		   },
		   {
		    "range": {
		     "@timestamp": {
		      "gte": "1521353712139",
		      "lte": "1521440112139",
		      "format": "epoch_millis"
		     }
		    }
		   }
		  ],
		  "must_not": []
		 }
		},
		"size": 0,
		"aggs": {
		 "tag_name": {
		  "date_histogram": {
		   "field": "@timestamp",
		   "interval": "30m",
		   "time_zone": "Pacific/Honolulu",
		   "min_doc_count": 1
		  }
		 }
		} 
	}
	return body

def sample_json2():
	'''json from qbox example'''
	body = {
		"query": {
		 "filtered": {
		  "query": {
		   "query_string": {
		    "query": "*",
		    "analyze_wildcard": "true"
		   }
		  },
		  "filter": {
		   "bool": {
		    "must": [
		     {
		      "range": {
		       "@timestamp": {
		        "gte": "now-12M",
		        "lte": "now",
		        "format": "epoch_millis"
		       }
		      }
		     }
		    ],
		    "must_not":[]
		   }
		  }
		 }
		},
		"size": 0,
		"aggs": {
		 "tag_name": {
		  "terms": {
		   "field": "remote_ip.raw",
		   "size": 1000,
		   "order": {
		    "_count": "desc"
		   }
		  }
		 }
		}
	}
	return body


def run_search(fxn):
	#dsl = dsl_equivalent_from_json(fxn)
	s.query(fxn)
	response = s.execute()
	if not response.success(): print("partial result")
	
	pprint.pprint(response)

	for hit in response['hits']['hits']:
		print(hit['_score'], hit['_source']['title'])

	#for tag in response['aggregations']['tag_name']['buckets']:
	#	print(tag['key'])	


#####################################################################
if __name__ == "__main__":
	client = elastic_connection_dsl()
	s = Search(using=client)
	run_search(sample_json1())
	



# s = s.doc_type('logs')
# beats = s.query("match", tags="beat")

# beats = s.filter('match', tags='beat').filter('range', _timestamp={'from', date(2018, 3, 17) } )


#q = Q('match', tags='beats') & Q('match', host='kphc-srvapp02')

#f = F('term', tags='beat') | F('range', _timestamp={'gte': date(2018, 3, 10) } )

#json_equivalent_from_dsl(q)

#a = search.aggs.bucket("logs_per_month", "date_histogram", field='@timestamp', interval="1M", format="yyyy-MM-dd")
