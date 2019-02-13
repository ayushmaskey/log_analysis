import pandas as pd
import matplotlib.pyplot as plt

from csv_to_pandas import csv_into_dict_of_data
from wavelet_transformation import csv_into_wavelet_transformed_dict_of_dataframe

import sys
sys.path.append('../elastic/')
from es_to_csv import dir_exists, file_exists

root = "../../"

def plot_dict_of_df_into_graph_and_save(df_dict, identifier):
	save_dir = root + "plots/"

	key_list = list(df_dict.keys() )

	
	if dir_exists(save_dir):
	
		for keys in key_list:
			df_dict[keys].plot(legend = False)
			plt.title(keys + "_traffic" + identifier)
			fileName = save_dir + keys + identifier + ".png"

			if file_exists(fileName):
				plt.savefig(fileName)
			# plt.show()
			plt.close()
	return



def wavelet_tranformation_DWT(level):
	
	# plot graph before any transformation
	df_dict = csv_into_dict_of_data()

	identifier = "_before_transformation"
	plot_dict_of_df_into_graph_and_save(df_dict, identifier)


	#plot graph after multiple levels of transformation
	wavelet_to_use = 'db1'
	for i in range(1,level):
		df_dict = csv_into_wavelet_transformed_dict_of_dataframe(wavelet_to_use, i)

		identifier = "_discrete_wavelet_transform_level_" + str(i)
		plot_dict_of_df_into_graph_and_save(df_dict, identifier)



def test():
	
	wavelet_tranformation_DWT(7)

if __name__ == "__main__":

	test()