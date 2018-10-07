
from es_connection import es_connect
import pandas as pd
import iso8601
import datetime as dt
from hashlib import sha1

from es_request_total_json import json_query
from es_request_protocol_json import json_protocol_query
from es_request_external_json import json_external_query
from es_request_2tags_3aggs_json import json_three_level_agg_query_two_tags

from es_aggregate_structure_json import agg_firewall_external_dest

#private API --> splir server_name to domain name
def domain_name(str):
	str = str.split(".")
	if len(str) >=2:
		str = str[-2] + "." + str[-1]
	return str


#private API --> flatten nest aggs response from elastic
def elasticAggsToDataframe(elasticResult,aggStructure,record={},fulllist=[]):
	"""
		https://stackoverflow.com/questions/29280480/pandas-dataframe-from-a-nested-dictionary-elasticsearch-result
		recursively flatten elastic result into dataframe
		takes elastic response as input along with aggregate structure
		aggStructure defines what to expect from response
	"""
	for agg in aggStructure:
		buckets = elasticResult[agg['key']]['buckets']
		for bucket in buckets:
			record = record.copy()
			record[agg['key']] = bucket['key']
			if 'aggs' in agg: 
				elasticAggsToDataframe(bucket,agg['aggs'],record,fulllist)
			else: 
				for var in agg['variables']:
					record[var['dfName']] = bucket[var['elasticName']]

				fulllist.append(record)
	df = pd.DataFrame(fulllist)
	return df

# private API --> convert es response to dataframe, only one level agg
def get_pandas_dataframe(aggsList):
	"""
		take aggregate response and convert to pandas dataframe
		timeseries dataframe with 
			timeseries index, 
			protocol used and 
			total traffic for the protocol
	"""
	df = pd.DataFrame(aggsList)

	df.columns = ['Total', 'unix_time', 'iso_time']	

	df["iso_time"] = df.iso_time.apply(iso8601.parse_date)
	df["Date"] = df["iso_time"].dt.date
	df["Time"] = df["iso_time"].dt.time
	df.index = df["Time"]
	df = df[['Date','Total'] ]

	return df


# public API --> connect to es, get one level agg and save to csv 
def es_traffic_pandas_csv(ind, start, end):
	"""
		figure out which JSON file to use
		Connect to elasticsearch
		search elastic using JSON File and body
		tease out the aggs and to be converted to dataframe
		save to csv file 
	"""

	if ind == "*":
		q = json_query(ind, start , end)
	elif ind == "external":
		q = json_external_query(ind, start, end)
	else:
		q = json_protocol_query(ind, start , end)
	
	es = es_connect()

	es_response = es.search(index="*", body=q)
	
	agg_list = es_response['aggregations']['total_traffic']['buckets']
	df = get_pandas_dataframe(agg_list)

	return df


#public API --> 
def es_nested_agg_pandas(start, end, agg1, agg2, agg3, tag1, tag2):
	es = es_connect()

	aggStructure = agg_firewall_external_dest()

	q = json_three_level_agg_query_two_tags(start, end, agg1, agg2, agg3, tag1, tag2)

	es_response = es.search(index="*", body=q)
	agg_list = es_response['aggregations']

	df = elasticAggsToDataframe(agg_list, aggStructure)
	
	if tag1 == "external_destination":
		df['URL'] = [domain_name(val) for val in df['server_name'] ]
	elif tag1 == "internal_destination":
		df['URL'] = [val.replace(".kphc.org","") for val in df['server_name']]


	df['sha1'] = [sha1(str(val).encode('utf-8')).hexdigest() for val in df['dest_ip']]
	df.index = df['sha1']

	df.drop_duplicates(subset=['dest_ip','dest_port', 'URL'], keep = False)

	return df	

#testing only
def test_main():
	start = "now-2d"
	end = "now"
	df = es_traffic_pandas_csv("*", start, end)
	print(df)

def test2():
	start = "now-2d"
	end = "now"
	df = es_nested_agg_pandas(start, end, 
			"destination_ips.keyword","destination_port","server_name.keyword",
			"internal_destination","internal_source")
	print(df)

if __name__ == "__main__":

	test2()
	