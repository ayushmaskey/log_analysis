from json_response import response_7d_15min


import dateutil.parser
import numpy as np
import pywt
from pywt import wavedec

import matplotlib
# print(matplotlib.get_backend())
matplotlib.use('Agg')
import matplotlib.pyplot as plt

unix_date = []
iso8601_date = []
total_traffic = []
std_date = []

def agg_to_numpy_ndarray(agg_list_of_dict):
	l =len(agg_list_of_dict)
	x = np.zeros(l)
	y = np.zeros(l)
	dt = dtype([('date', 'int'), ('total', 'int')] )
	arrays = np.array(list(agg_15min_list['key'], 
		agg_15min_list['doc_count'] ),
		dtype=dt )
	# arrays = {'unix_date': np.array(agg_list_of_dict['key'], dtype=int), 'total': np.array(agg_15min_list['doc_count'], dtype=int) }
	return arrays

def agg_to_matplotlib_list(agg_list_of_dict):
	for agg_15min_list in agg_list_of_dict:
		unix_date.append(agg_15min_list['key'])
		iso8601_date.append(agg_15min_list['key_as_string'])
		total_traffic.append(agg_15min_list['doc_count'])
		std_date.append(dateutil.parser.parse(agg_15min_list['key_as_string']))

def show(plt):
	plt.xlabel('time')
	plt.ylabel('total traffic')
	plt.title('graph') 
	plt.legend()
	plt.show()

def line_graph(x, y):
	plt.plot(x, y, label="total_traffic")
	show(plt)

def bar_graph(x, y):
	plt.bar(x, y)
	show(plt)
	

if __name__ == "__main__":
	resp_dict = response_7d_15min()
	agg_list = resp_dict['aggregations']['total_traffic']['buckets']
	agg_to_matplotlib_list(agg_list)
	
	line_graph(std_date,total_traffic)
	# coeff = pywt.dwt(total_traffic, 'db1', level=5
	coeff = wavedec(total_traffic, 'db1', level=5)
	print(coeff)
	# agg_to_numpy_ndarray(agg_list)
