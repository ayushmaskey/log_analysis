import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

from csv_to_pandas import csv_into_dict_of_data
from wavelet_transformation import csv_into_wavelet_transformed_dict_of_dataframe

from kmeans_elbow import find_k_for_KMeans_elbow_method_score as elbow
from constants import start, end, training_dataset, plot_save_dir, wavelet_to_use

import sys
sys.path.append('../elastic/')
from es_to_csv import dir_exists, file_exists

from pprint import pprint



def plot_troffic_graph_df_into_graph_and_save(df_dict, identifier):
	# plot_save_dir = root + "plots/"

	key_list = list(df_dict.keys() )
	wavelet_dir = "wavelet/" 
	
	if dir_exists(plot_save_dir):
	
		for keys in key_list:
			df_dict[keys].plot(legend = False)
			plt.title(keys + "_traffic" + identifier)
			plt.grid(True)
			plt.xlabel('15 minute interval')
			plt.ylabel('# of document generated')
			fileName = plot_save_dir + wavelet_dir + keys + identifier + ".png"

			if file_exists(fileName):
				plt.savefig(fileName)
			# plt.show()
			plt.close()
	return

def plot_elbow(df_dict, id):
	key_list = list(df_dict.keys() )
	elbow_dir = "elbow/"

	for key in key_list:
		score = elbow(df_dict[key])
		identifier = "elbow_curve_" + key + id

		num_cluster = range(start, end)

		fig = plt.figure(figsize=(15, 5))
		plt.plot(num_cluster,score)
		plt.xlabel('Number of Clusters')
		plt.ylabel('Score')
		plt.grid(True)
		plt.title(identifier)

		fileName = plot_save_dir + elbow_dir + identifier + ".png"
		print(fileName)
		if file_exists(fileName):
			plt.savefig(fileName)
		# plt.show()
		plt.close()
	return



def df_after_transformation():
	
	#plot graph after multiple levels of transformation
	level = 7

	for pywt in wavelet_to_use:
		for i in range(1,level):
			df_dict = csv_into_wavelet_transformed_dict_of_dataframe(pywt, i, training_dataset)

			identifier = "_" + pywt + "_wavelet_transform_level_" + str(i)
			plot_troffic_graph_df_into_graph_and_save(df_dict, identifier)
			print(identifier)

			if i < 4:
				plot_elbow(df_dict, identifier)



def df_before_transformation():
	# plot graph before any transformation
	df_dict = csv_into_dict_of_data(training_dataset)
	identifier = "_before_transformation"
	plot_troffic_graph_df_into_graph_and_save(df_dict, identifier)
	plot_elbow(df_dict, identifier)




if __name__ == "__main__":

	df_before_transformation()
	df_after_transformation()
