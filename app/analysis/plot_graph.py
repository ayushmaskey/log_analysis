import pandas as pd
import matplotlib.pyplot as plt

from csv_to_pandas import dictionary_of_dataframes
from wavelet_transformation import dictOfDictOfList_rawNumber_to_DWTApprox

import sys
sys.path.append('../elastic/')
from es_to_csv import dir_exists, file_exists

root = "../../"

def plot_graph_and_save(df_dict, identifier):
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
	df_dict = dictionary_of_dataframes()

	identifier = "_before_transformation"
	plot_graph_and_save(df_dict, identifier)


	#plot graph after multiple levels of transformation
	wavelet_to_use = 'db1'
	for i in range(1,level):
		df_dict = dictOfDictOfList_rawNumber_to_DWTApprox(wavelet_to_use, i)

		identifier = "_discrete_wavelet_transform_level_" + str(i)
		plot_graph_and_save(df_dict, identifier)



def test():
	
	wavelet_tranformation_DWT(7)

if __name__ == "__main__":

	test()