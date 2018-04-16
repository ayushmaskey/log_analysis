
from es_pickle import unpickle_data
from es_pandas import es_traffic_pandas_pickle

fileName = './pickle/test.pickle'

def push_to_pickle():
	ind = "*"
	start = "now-2d/d"
	end = "now-2d/d"
	
	es_traffic_pandas_pickle(fileName, ind, start, end)

def get_from_pickle():
	pd_dict = unpickle_data(fileName)
	return pd_dict

if __name__ == "__main__":
	pd_dict = unpickle_data(fileName)