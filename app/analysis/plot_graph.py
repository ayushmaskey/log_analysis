import pandas as pd
import matplotlib.pyplot as plt

from csv_to_pandas import dictionary_of_dataframes
from wavelet_transformation import dictOdDictOfList_rawNumber_to_DWTApprox

import sys
sys.path.append('../elastic/')
from es_to_csv import dir_exists, file_exists


def plot_graph_and_save(root, df_dict, identifier):
	save_dir = root + "plots/"

	key_list = list(df_dict.keys() )

	
	if dir_exists(save_dir):
	
		for keys in key_list:
			df_dict[keys].plot(legend = False)
			plt.title(keys + "traffic" + identifier)
			fileName = save_dir + keys + identifier + ".png"

			if file_exists(fileName):
				plt.savefig(fileName)
			# plt.show()
			plt.close()
	return


def time_series_graph(root):
	# csv_path = root + "csv"

	df_dict = dictionary_of_dataframes()

	identifier = "_wo_transformation"
	plot_graph_and_save(root, df_dict, identifier)


def single_level_DWT(root):
	wavelet_to_use = 'db1'
	for i in range(1,5):
		df_dict = dictOdDictOfList_rawNumber_to_DWTApprox(wavelet_to_use, i)

		identifier = "_discrete_wavelet_transform_level_" + str(i)
		plot_graph_and_save(root, df_dict, identifier)



def test():
	root = "../../"
	time_series_graph(root)
	single_level_DWT(root)

if __name__ == "__main__":

	test()