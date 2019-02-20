import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

from sklearn.cluster import KMeans, MeanShift
from sklearn.externals import joblib

from csv_to_pandas import csv_into_dict_of_data
from wavelet_transformation import csv_into_wavelet_transformed_dict_of_dataframe
from constants import training_dataset, model_save_dir, wavelet_to_use

#algorithm
def semi_unsupervised_KMeans(df, num_clusters):
	
	km = KMeans(n_clusters = num_clusters)
	km.fit(df)
	return km 

def unsupervised_heirarchial_MeanShift(df, num_clusters):
	#MeanShift accurate up to 10,000 data points
	ms = MeanShift()
	ms.fit(df)
	return ms


def training(algo, df_dict, str1, str2):
	
	key_list = list(df_dict.keys())
	for key in key_list:
		df = df_dict[key]
		df = df.reindex(sorted(df.columns), axis = 1)

		df_dict[key] = df

		cluster_model = algo(df_dict[key], 3)
		filename = model_save_dir + str1 + key + str2 + ".pkl"
		print(filename)
		_ = joblib.dump(cluster_model, filename, compress=9)
		


def test_print(model):
	centroids = km.cluster_centers_ 
	labels = km.labels_
	inertia = km.inertia_

	print('KMeans', key)
	print('Centroids: ', centroids)
	print('Labels:',labels)
	print('Inertia: ', inertia)
	print('num of interation: ', km.n_iter_ )

def test_new_df_dict():
	df_dict = training()

	key_list = list(df_dict.keys())
	print(key_list)
	for key in key_list:
		print(key, list(df_dict[key].columns))

def start_training():

	str_kmeans = "kmeans_model_"
	str_meanshift = "meanshift_model_"

	str_no_transform = "_before_transformation"
	df_dict = csv_into_dict_of_data(training_dataset)

	training(semi_unsupervised_KMeans, df_dict, str_kmeans, str_no_transform)
	training(unsupervised_heirarchial_MeanShift, df_dict, str_meanshift, str_no_transform)


	level = 4

	for pywt in wavelet_to_use:
		for i in range(1,level):
			df_dict = csv_into_wavelet_transformed_dict_of_dataframe(pywt, i, training_dataset)
		
			str_transformation = "_" + pywt + "_wavelet_transform_level_" + str(i)

			training(semi_unsupervised_KMeans, df_dict, str_kmeans, str_transformation)
			training(unsupervised_heirarchial_MeanShift, df_dict, str_meanshift, str_transformation)			



if __name__ == "__main__":
	start_training()