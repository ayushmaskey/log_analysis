
from es_pickle import unpickle_data
from es_pandas import es_traffic_pandas_pickle
from scipy.spatial import distance

def get_data():
	fileName = './pickle/test.pickle'

	pd_list = unpickle_data(fileName)
	# print(pd_list)
	for k, df in pd_list.items():
		print(k, df)
	# return pd_list




if __name__ == "__main__":
	get_data()