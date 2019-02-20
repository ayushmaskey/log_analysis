import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

from sklearn.cluster import KMeans, MeanShift

from csv_to_pandas import csv_into_dict_of_data
from wavelet_transformation import csv_into_wavelet_transformed_dict_of_dataframe


#algorithm
def semi_unsupervised_KMeans(df, num_clusters):
	
	km = KMeans(n_clusters = num_clusters)
	km.fit(df)
		# centroids = km.cluster_centers_ 
	# labels = km.labels_
	# inertia = km.inertia_

	# print('KMeans')
	# print('Centroids: ', centroids)
	# print('Labels:',labels)
	# print('Inertia: ', inertia)
	# print('num of interation: ', km.n_iter_ )

	# prediction = km.predict(df1)
	# print(prediction)
	return km 

def unsupervised_heirarchial_MeanShift(df):
	#MeanShift accurate up to 10,000 data points
	ms = MeanShift()
	ms.fit(df)

	# labels = ms.labels_
	# centroid_lite = ms.cluster_centers_
	# n_clusters = len(set(labels))

	# print('MeanShift')
	# print('Labels:',labels)
	# print('Centroid Lite:',centroid_lite)
	# print(n_clusters)

	return ms


# prepping the data
def reorganize_data(df, new_list):
	df = df[new_list]
	df = df.reindex(sorted(df.columns), axis = 1)
	return df

def get_training_dataset(df):
	column_list = [col for col in df.columns if col < '2019-02-01']
	df = reorganize_data(df, column_list)
	return df

def get_validation_dataset(df):
	column_list = [col for col in df.columns if col >= '2019-03-01']
	df = reorganize_data(df, column_list)
	return df


def training():
	df_dict = csv_into_dict_of_data()
	
	key_list = list(df_dict.keys())
	for key in key_list:
		df = get_training_dataset(df_dict[key])
		df_dict[key] = df

		km = semi_unsupervised_KMeans(df_dict[key], 3)

		centroids = km.cluster_centers_ 
		labels = km.labels_
		inertia = km.inertia_

		print('KMeans')
		print('Centroids: ', centroids)
		print('Labels:',labels)
		print('Inertia: ', inertia)
		print('num of interation: ', km.n_iter_ )

	return df_dict

def test_new_df_dict():
	df_dict = training()

	key_list = list(df_dict.keys())
	print(key_list)
	for key in key_list:
		print(key, list(df_dict[key].columns))


if __name__ == "__main__":

	training()