import pandas as pd
import matplotlib.pyplot as plt

from csv_to_pandas import dictionary_of_dataframes

import sys
sys.path.append('../elastic/')
from es_to_csv import dir_exists, file_exists


def plot_graph_and_save(root, df_dict, identifer):
	save_dir = root + "plots/"

	key_list = list(df_dict.keys() )

	
	if dir_exists(save_dir):
	
		for keys in key_list:
			df_dict[keys].plot(legend = False)
			plt.title(keys + " traffic")
			fileName = save_dir + keys + identifer + ".png"

			if file_exists(fileName):
				plt.savefig(fileName)
			# plt.show()
	return



def test():
	root = "../../"
	csv_path = root + "csv"

	df_dict = dictionary_of_dataframes()

	identifer = "_wo_transformation"
	plot_graph_and_save(root, df_dict, identifer)




if __name__ == "__main__":

	test()