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
			df_dict[keys].plot(legend = False, figsize=(30, 15))
			plt.title(keys + "_traffic" + identifier)
			plt.grid(True)
			plt.xlabel('15 minute interval')
			plt.ylabel('# of document generated')
			fileName = plot_save_dir + wavelet_dir + keys + identifier + ".png"

			print(fileName)
			if file_exists(fileName):
				plt.savefig(fileName)
			# plt.show()
			plt.close('all')
	return


def plot_elbow(score, elbow_dir, identifier):
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

def get_elbow_by_date_and_time(df_dict, id):
	key_list = list(df_dict.keys() )
	elbow_date_dir = "elbow_date/"
	elbow_time_dir = "elbow_time/"

	for key in key_list:
		identifier = "elbow_curve_by_date_" + key + id
		score_by_date = elbow(df_dict[key].T)
		plot_elbow(score_by_date, elbow_date_dir, identifier)

		identifier = "elbow_curve_by_time_" + key + id
		score_by_time = elbow(df_dict[key])
		plot_elbow(score_by_time, elbow_time_dir, identifier)		
		
	return


def remove_zero_columns(df_dict):
	key_list = list(df_dict.keys())
	
	for key in key_list:
		df = df_dict[key]
		df = df.loc[ :, (df > 10).any(axis=0) ]
		df_dict[key] = df

	return df_dict

def df_after_transformation():
	
	#plot graph after multiple levels of transformation
	level = 7

	for pywt in wavelet_to_use:
		for i in range(1,level):
			df_dict = csv_into_wavelet_transformed_dict_of_dataframe(pywt, i, training_dataset)
			df_dict = remove_zero_columns(df_dict)

			identifier = "_" + pywt + "_wavelet_transform_level_" + str(i)
			plot_troffic_graph_df_into_graph_and_save(df_dict, identifier)
			print(identifier)

			if i < 4:
				get_elbow_by_date_and_time(df_dict, identifier)



def df_before_transformation():
	"""plot graph before any transformation"""
	df_dict = csv_into_dict_of_data(training_dataset)
	df_dict = remove_zero_columns(df_dict)
	identifier = "_before_transformation"
	plot_troffic_graph_df_into_graph_and_save(df_dict, identifier)
	get_elbow_by_date_and_time(df_dict, identifier)

	# print(df_dict)




if __name__ == "__main__":

	df_before_transformation()
	df_after_transformation()
