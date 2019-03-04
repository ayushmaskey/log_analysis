import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

from sklearn.cluster import KMeans, MeanShift, DBSCAN
from sklearn.externals import joblib

from csv_to_pandas import csv_into_dict_of_data
from wavelet_transformation import csv_into_wavelet_transformed_dict_of_dataframe
from constants import testing_dataset, model_save_dir
from plot_graph import remove_zero_columns
from training_cluster import plot_cluster_model,save_dataframe_with_cluster

import sys
sys.path.append('../elastic/')
from es_to_csv import dir_exists, file_exists

before_transformation = '_before_transformation.pkl'
date_model_loc = 'cluster_date_model/'
time_model_loc = 'cluster_time_model/'

def testing_dataset_with_saved_model(df, key, model_loc):
	ms_model_path = model_save_dir + model_loc + 'meanshift_model_'+ key + before_transformation
	km_model_path = model_save_dir + model_loc + 'kmeans_model_' + key + before_transformation

	ms_model = joblib.load(ms_model_path)
	km_model = joblib.load(km_model_path)

	ms_prediction = ms_model.predict(df)
	km_prediction = km_model.predict(df)
	
	str2 = "_before_transformation"
	plot_cluster_model(df, ms_prediction, key, 'meanshift_model_', str2, 'dates', 'testing_cluster/')
	plot_cluster_model(df, km_prediction, key, 'kmeans_model_', str2, 'dates', 'testing_cluster/')

	df_ms = df.copy()
	df_ms['cluster'] = ms_prediction
	
	df_km = df.copy()
	df_km['cluster'] = km_prediction

	df_ms_filename = model_save_dir + "testing_dataframe/" + 'meanshift_model_' + key + "_testing_dataframe_by_date.pkl"
	df_km_filename = model_save_dir + "testing_dataframe/" + 'kmeans_model_' + key + "_testing_dataframe_by_date.pkl"
	
	save_dataframe_with_cluster(df_ms, df_ms_filename)
	save_dataframe_with_cluster(df_km, df_km_filename)



def testing_february():
	df_dict = csv_into_dict_of_data(testing_dataset)
	df_dict = remove_zero_columns(df_dict)

	df_pivot = {}


	key_list = list(df_dict.keys())
	for key in key_list:
		df = df_dict[key]
		df = df.reindex(sorted(df.columns), axis = 1)

		df_dict[key] = df
		df_pivot[key] = df_dict[key].T 

		# testtin_dataset_with_saved_model(df_dict[key], key, time_model_loc)
		testing_dataset_with_saved_model(df_pivot[key], key, date_model_loc)

		

if __name__ == "__main__":

	testing_february()