
from es_connection import es_connect
from es_request_json import json_query
import pandas as pd
from es_pickle import pickle_data

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
	df = df[['total_traffic', 'unix_time'] ]

	return df

def es_traffic_pandas_pickle(fileName, ind, start, end):
	df = get_pandas_dataframe(ind, start, end)
	pickle_data(fileName, df) 



if __name__ == "__main__":

	ind = "*"
	start = "now-3d/d"
	end = "now-3d/d"
	fileName = './pickle/test.pickle'

	pkl = es_traffic_pandas_pickle(fileName, ind, start, end)
	# pickle_data(fileName, df)