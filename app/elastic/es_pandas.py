
from es_connection import es_connect
from es_request_total_json import json_query
import pandas as pd
from es_to_csv import append_to_csv
import iso8601
import datetime as dt


def get_agg_response_list_of_dict(ind, start, end ):
	
	es = es_connect()
	q = json_query(ind, start , end)
	es_response = es.search(index=ind, body=q)
	
	agg_list = es_response['aggregations']['total_traffic']['buckets']
	
	return agg_list


def get_pandas_dataframe(ind, start, end):
	lists_dict = get_agg_response_list_of_dict(ind, start, end)

	df = pd.DataFrame(lists_dict)

	df.columns = ['Total', 'unix_time', 'iso_time']	

	df["iso_time"] = df.iso_time.apply(iso8601.parse_date)
	df["Date"] = df["iso_time"].dt.date
	df["Time"] = df["iso_time"].dt.time
	df.index = df["Time"]
	df = df[['Date','Total'] ]

	return df

def es_traffic_pandas_csv(fileName, ind, start, end):
	df = get_pandas_dataframe(ind, start, end)
	append_to_csv(fileName, df)


if __name__ == "__main__":


	ind = "*"
	start = "now-1d"
	end = "now"


	fileName = 'test'

	
	es_traffic_pandas_csv(fileName, ind, start, end)
	#get_pandas_dataframe(ind, start, end)