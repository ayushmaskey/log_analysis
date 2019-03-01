import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

from sklearn.cluster import KMeans, MeanShift
from sklearn.externals import joblib

from csv_to_pandas import csv_into_dict_of_data
from wavelet_transformation import csv_into_wavelet_transformed_dict_of_dataframe
from constants import training_dataset, model_save_dir, wavelet_to_use, k_in_kmeans

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


def training(algo, df_dict, str1, str2, k_dict):
	
	key_list = list(df_dict.keys())
	for key in key_list:
		df = df_dict[key]
		df = df.reindex(sorted(df.columns), axis = 1)

		k = k_dict[key]

		df_dict[key] = df

		cluster_model = algo(df_dict[key], k)
		filename = model_save_dir + str1 + key + str2 + ".pkl"
		print(filename)
		_ = joblib.dump(cluster_model, filename, compress=9)
		


def testing():
	k_dict = k_in_kmeans["before"]
	print(k["dns"])

def start_training():

	str_kmeans = "kmeans_model_"
	str_meanshift = "meanshift_model_"

	str_no_transform = "_before_transformation"
	df_dict = csv_into_dict_of_data(training_dataset)

	k_dict = k_in_kmeans["before"]

	training(semi_unsupervised_KMeans, df_dict, str_kmeans, str_no_transform, k_dict)
	training(unsupervised_heirarchial_MeanShift, df_dict, str_meanshift, str_no_transform, k_dict )


	level = 4

	for pywt in wavelet_to_use:
		for i in range(1,level):
			df_dict = csv_into_wavelet_transformed_dict_of_dataframe(pywt, i, training_dataset)
		
			str_transformation = "_" + pywt + "_wavelet_transform_level_" + str(i)

			training(semi_unsupervised_KMeans, df_dict, str_kmeans, str_transformation, k_dict)
			training(unsupervised_heirarchial_MeanShift, df_dict, str_meanshift, str_transformation, k_dict)			



if __name__ == "__main__":
	start_training()