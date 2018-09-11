
from es_connection import es_connect
from es_request_json import json_query
import pandas as pd
from es_csv import append_to_csv

def get_agg_response_list_of_dict(ind, start, end ):
	
	es = es_connect()
	q = json_query(ind, start , end)
	es_response = es.search(index=ind, body=q)
	
	agg_list = es_response['aggregations']['total_traffic']['buckets']
	
	return agg_list


def get_pandas_dataframe(ind, start, end):
	lists_dict = get_agg_response_list_of_dict(ind, start, end)

	df = pd.DataFrame(lists_dict)

	df.columns = ['total_traffic', 'unix_time', 'iso_time']
	df.index = pd.to_datetime(df.iso_time)
	df.index.names = ['DateTimeIndex']
	df = df[['total_traffic'] ]

	return df

def es_traffic_pandas_csv(fileName, ind, start, end):
	df = get_pandas_dataframe(ind, start, end)
	append_to_csv(fileName, df)
	# print(df)


if __name__ == "__main__":


	ind = "*"
	start = "now-1d/d"
	end = "now-1d/d"

	csv_file_path = '../csv/'
	csv_file_name = 'test.csv'
	fileName = csv_file_path + csv_file_name

	
	es_traffic_pandas_csv(fileName, ind, start, end)