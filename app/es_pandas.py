
from es_connection import es_connect
from es_request_json import json_query
import pandas as pd


def get_agg_response_list_of_dict(ind, start, end ):
	es = es_connect()
	q = json_query(ind, start , end)
	es_response = es.search(index=ind, body=q)
	agg_list = es_response['aggregations']['total_traffic']['buckets']
	return agg_list


def get_pandas_datafrane(ind, start, end):
	lists_dict = get_agg_response_list_of_dict(ind, start, end)
	df = pd.DataFrame(lists_dict)
	return df

if __name__ == "__main__":
	ind = "*"
	start = "now-1d"
	end = "now"
	df = get_pandas_datafrane(ind, start, end)
	print(df)