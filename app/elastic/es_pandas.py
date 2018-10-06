
from es_connection import es_connect
import pandas as pd
import iso8601
import datetime as dt

from es_request_total_json import json_query
from es_request_protocol_json import json_protocol_query
from es_request_external_json import json_external_query




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
		Connect to elasticsearch
		figure out which JSON file to use
		search elastic using JSON File and body
		tease out the aggs and to be converted to dataframe
		save to csv file 
	"""
	es = es_connect()

	if ind == "*":
		q = json_query(ind, start , end)
	elif ind == "external":
		q = json_external_query(ind, start, end)
	else:
		q = json_protocol_query(ind, start , end)

	es_response = es.search(index="*", body=q)
	
	agg_list = es_response['aggregations']['total_traffic']['buckets']
	df = get_pandas_dataframe(agg_list)

	return df


def test_main():
	start = "now-2d"
	end = "now"
	df = es_traffic_pandas_csv("*", start, end)
	print(df)

if __name__ == "__main__":

	test_main()
	