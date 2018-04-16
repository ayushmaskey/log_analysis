
from es_pickle import unpickle_data
from es_pandas import es_traffic_pandas_pickle
from pprint import pprint

fileName = './pickle/test.pickle'

def push_to_pickle():
	ind = "*"
	start = "now-6d/d"
	end = "now-6d/d"
	
	es_traffic_pandas_pickle(fileName, ind, start, end)

def get_from_pickle():
	pd_dict = unpickle_data(fileName)
	return pd_dict

if __name__ == "__main__":
	push_to_pickle()