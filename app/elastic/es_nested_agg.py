

from es_connection import es_connect
from es_request_firewall_outside_json import json_firewall_outside_query
from pprint import pprint

#https://stackoverflow.com/questions/29280480/pandas-dataframe-from-a-nested-dictionary-elasticsearch-result
import pandas as pd
def elasticToDataframe(elasticResult,aggStructure,record={},fulllist=[]):
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




# aggStructure=[{'key':'xColor','aggs':[{'key':'xMake','aggs':[{'key':'xCity','variables':[{'elasticName':'doc_count','dfName':'count'}]}]}]}]

aggStructure=[{'key':'dest_ip','aggs':[{'key':'dest_port','aggs':[{'key':'server_name','variables':[{'elasticName':'doc_count','dfName':'count'}]}]}]}]

start = "now-1d"
end = "now"	
ind = "bro_dns"
all_index = "*"

es = es_connect()
q = json_firewall_outside_query(ind, start , end)
es_response = es.search(index=all_index, body=q)

resp_agg = es_response['aggregations']

x = elasticToDataframe(resp_agg,aggStructure)

