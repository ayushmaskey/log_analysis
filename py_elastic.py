from elasticsearch import Elasticsearch
from request_json import total_traffic_count_30m_interval, sample_json2

import click
import json

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


@click.command()
@click.argument('query', required=True)
@click.option('---raw-result/---no-ra-result', default=False)
def search(query, raw_result):
	es = elastic_connection_py()
	matches = es.search('*', q=query)
	hits = matches['hits']['hits']
	if not hits:
		click.echo('no matches found')
	else:
		if raw_result:
			click.echo(json.dumps(matches, indent=4))
		for hit in hits:
			click.echo('Subject:{}\nPath:{}\n\n'.format(
				hit['_source']['subject'],
				hit['_source']['path']
			))
#####################################################################
if __name__ == "__main__":
	
	client = elastic_connection_py()
	query = total_traffic_count_30m_interval()
	result= client.search(index="*", body=query)	

#	search(query)

	print(result)


