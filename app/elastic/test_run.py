
from es_connection import es_connect
import pandas as pd
import iso8601
import datetime as dt
from pprint import pprint

from es_request_total_json import json_query
from es_request_protocol_json import json_protocol_query
from es_request_external_json import json_external_query
from es_request_firewall_outside_json import json_firewall_outside_query

from es_to_csv import append_to_csv


def get_agg_response_list_of_dict(ind, start, end ):
	
	all_index = "*"

	# es = es_connect()
	if ind == "*":
		q = json_query(ind, start , end)
	elif ind == "external":
		q = json_external_query(ind, start, end)
	else:
		q = json_protocol_query(ind, start , end)

	es_response = es.search(index=all_index, body=q)
	
	agg_list = es_response['aggregations']['total_traffic']['buckets']
	
	return agg_list


def get_pandas_dataframe(aggsList):

	df = pd.DataFrame(aggsList)

	df.columns = ['Total', 'unix_time', 'iso_time']	

	df["iso_time"] = df.iso_time.apply(iso8601.parse_date)
	df["Date"] = df["iso_time"].dt.date
	df["Time"] = df["iso_time"].dt.time
	df.index = df["Time"]
	df = df[['Date','Total'] ]

	return df

#https://stackoverflow.com/questions/29280480/pandas-dataframe-from-a-nested-dictionary-elasticsearch-result
import pandas as pd
def elasticAggsToDataframe(elasticResult,aggStructure,record={},fulllist=[]):
	for agg in aggStructure:
		buckets = elasticResult[agg['key']]['buckets']
		for bucket in buckets:
			record = record.copy()
			record[agg['key']] = bucket['key']
			if 'aggs' in agg: 
				elasticToDataframe(bucket,agg['aggs'],record,fulllist)
			else: 
				for var in agg['variables']:
					record[var['dfName']] = bucket[var['elasticName']]

				fulllist.append(record)
	df = pd.DataFrame(fulllist)
	return df

def es_traffic_pandas_csv(fileName, ind, start, end):
	#connect to elastic	
	es = es_connect()

	#find which json to use
	if ind == "*":
		q = json_query(ind, start , end)
	elif ind == "external":
		q = json_external_query(ind, start, end)
	else:
		q = json_protocol_query(ind, start , end)

	#search elastic
	es_response = es.search(index="*", body=q)
	
	#tease out the aggs and to be converted to datafrom
	agg_list = es_response['aggregations']['total_traffic']['buckets']
	df = get_pandas_dataframe(agg_list)

	# save to csv file 
	append_to_csv(fileName, df)


	
def es_simple_agg(start, end):
	ind = {
			"total": "*", 
			"dhcp": "bro_dhcp",
			"dns": "bro_dns",
			"conn": "bro_conn",
			"snmp": "bro_snmp",
			"weird": "bro_weird",
			"http": "bro_http",
			"files": "bro_files",
			"external": "external"
		}

	for key, value in ind.items():
		es_traffic_pandas_csv(key, value, start, end)

def load_main():
	start = "now-2d"
	end = "now"

	es_simple_agg(start, end)
	print("daily load on", dt.datetime.now() ,"successful!!")



def load_main2():
	start = "now-2d"
	end = "now"


	aggStructure1 = [
			{'key':'dest_ip',
			'aggs':[
				{'key':'dest_port',
				'aggs':[
					{'key':'server_name',
					'variables':[
						{'elasticName':'doc_count',
						'dfName':'count'
						}
					]
					}
				]
				}
			]
			}
		]

	# "firewall_eDst": aggStructure1

	
	#one aggregate
	

	print("daily load on", dt.datetime.now() ,"successful!!")


if __name__ == "__main__":
	load_main()