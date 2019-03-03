import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
import numpy as np
from collections import Counter

from sklearn.cluster import KMeans, MeanShift, DBSCAN
from sklearn.externals import joblib

from csv_to_pandas import csv_into_dict_of_data
from wavelet_transformation import csv_into_wavelet_transformed_dict_of_dataframe
from constants import training_dataset, model_save_dir, wavelet_to_use, k_in_kmeans_before, label_color_map,plot_save_dir
from plot_graph import remove_zero_columns
from es_to_csv import dir_exists, file_exists

algorithm = ''
#algorithm
def semi_unsupervised_KMeans(df, num_clusters):
	
	km = KMeans(n_clusters = num_clusters, init = 'k-means++', max_iter=300, random_state=0)
	km.fit(df)
	return km 

def unsupervised_heirarchial_MeanShift(df, num_clusters):
	#MeanShift accurate up to 10,000 data points
	ms = MeanShift()
	ms.fit(df)
	return ms


def dbscan_clustering(df, num_clusters):
	db = DBSCAN()
	db.fit(df)
	print(db)
	return db

def plot_cluster_model(df, labels, key, str1, str2, xlabel):
	
	color_scheme = []


	"""label into color"""
	for label in labels:
		color_scheme.append(label_color_map[label]) 

	"""count each color"""
	custom_legend = Counter(color_scheme)

	"""concatenate key and value of dict for legend"""
	custom_legend = ','.join( key + ' (' + str(value) + ')' for key, value in custom_legend.items() ) 
	custom_legend = custom_legend.split(",")

	# ax = df.plot(legend = True, figsize=(20,10), color = color_scheme)
	df.plot(legend = False, figsize=(20,10), color = color_scheme)
	plt.legend(custom_legend)

	if xlabel == 'dates':
		str3 = 'Each line represent time frame in 15 minute interval'
	elif xlabel == '15_minute_interval':
		str3 = 'Each line represent a day'


	plt.title( str1 + str2 + ' '+ key + '\n' + str3 )
	plt.grid(True)
	plt.xlabel(xlabel)
	plt.ylabel('# of document generated')

	fileName = plot_save_dir + 'training_cluster/' + str1 + key + str2 + '_' + 'cluster_colored_by_' + xlabel + ".png"
	print(fileName)

	if file_exists(fileName):
		plt.savefig(fileName)
	# plt.show()
	plt.close('all')

def training(algo, df_dict, str1, str2):
	df_dict = remove_zero_columns(df_dict)
	df_pivot = {}

	k_dict_date = k_in_kmeans_before['date']
	k_dict_time = k_in_kmeans_before['time']

	key_list = list(df_dict.keys())
	for key in key_list:
		df = df_dict[key]
		df = df.reindex(sorted(df.columns), axis = 1)
		

		df_dict[key] = df

		"""by date ie transformation/ pivot"""
		k = k_dict_date[key]
		df_pivot[key] = df_dict[key].T 
		cluster_model_date = algo(df_pivot[key], k)
		cluster_label = cluster_model_date.labels_

		plot_cluster_model(df_pivot[key], cluster_label, key, str1, str2, 'dates')


		df_pivot[key]['cluster'] = cluster_label

		filename = model_save_dir + "cluster_date_model/" + str1 + key + str2 + ".pkl"
		print(filename)
		_ = joblib.dump(cluster_model_date, filename, compress=9)

		df_filename = model_save_dir + "training_dataframe/" + str1 + "training_dataframe_by_date.pkl"
		print(df_filename)
		_ = joblib.dump(df_pivot, df_filename, compress=9)


		"""by time original that was messed up a bit"""
		k1 = k_dict_time[key]
		cluster_model_time = algo(df_dict[key], k1)
		cluster_label1 = cluster_model_time.labels_

		plot_cluster_model(df_dict[key], cluster_label, key, str1, str2, '15_minute_interval')


		df_dict[key]['cluster'] = cluster_label1

		filename2 = model_save_dir + "cluster_time_model/" + str1 + key + str2 + ".pkl"
		print(filename2)
		_ = joblib.dump(cluster_model_date, filename, compress=9)
		
		df_filename2 = model_save_dir + "training_dataframe/" + str1 + "training_dataframe_by_time.pkl"
		print(df_filename2)
		_ = joblib.dump(df_dict, df_filename2, compress=9)




str_kmeans = "kmeans_model_"
str_meanshift = "meanshift_model_"
str_dbscan = "dbscan_model_"

def before_transformation():
	str_no_transform = "_before_transformation"
	df_dict = csv_into_dict_of_data(training_dataset)


	training(semi_unsupervised_KMeans, df_dict, str_kmeans, str_no_transform)
	# training(unsupervised_heirarchial_MeanShift, df_dict, str_meanshift, str_no_transform )
	# training(dbscan_clustering, df_dict, str_kmeans, str_no_transform)


def after_transformation():
	level = 4
	k_dict = k_in_kmeans["before"]

	for pywt in wavelet_to_use:
		for i in range(1,level):
			df_dict = csv_into_wavelet_transformed_dict_of_dataframe(pywt, i, training_dataset)
		
			str_transformation = "_" + pywt + "_wavelet_transform_level_" + str(i)

			training(semi_unsupervised_KMeans, df_dict, str_kmeans, str_transformation, k_dict)
			training(unsupervised_heirarchial_MeanShift, df_dict, str_meanshift, str_transformation, k_dict)			

def start_training():
	before_transformation()
	after_transformation()


if __name__ == "__main__":
	before_transformation()