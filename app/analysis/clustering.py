import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans, MeanShift

#dict of dataframe without transformation 
from csv_to_pandas import csv_into_dict_of_data

#dict of dataframe after transformation
from wavelet_transformation import csv_into_wavelet_transformed_dict_of_dataframe

#number of k for kmeans elbow
start = 1
end = 10


# fnding elbow
def find_k_for_KMeans_elbow_method_sum_of_square_to_nearest_centroid(df):
	distortions = []
	for k in range(start, end):
		km = KMeans(n_clusters = k)
		km.fit(df)
		distortions.append(km.inertia_)
	print(distortions)
	# Plot the elbow
	fig = plt.figure(figsize=(15, 5))
	plt.plot(range(start, end), distortions)
	plt.xlabel('Number of Clusters')
	plt.ylabel('distortions')
	plt.grid(True)
	plt.title('Elbow Method to find k using inertia_')
	plt.show()

def find_k_for_KMeans_elbow_method_score(df):
	Nc = range(start, end)

	km = [KMeans(n_clusters=i) for i in Nc]
	score = [km[i].fit(df).score(df) for i in range(len(km))]
	return score




if __name__ == "__main__":

	df_dict = dictionary_of_dataframes()
	key_list = list(df_dict.keys())


	df = df_dict['dhcp']
	num_clusters = 3

	# find_k_for_KMeans_elbow_method2(df)
	# find_k_for_KMeans_elbow_method_sum_of_square_to_nearest_centroid(df)


	semi_unsupervised_KMeans(df, num_clusters)

	# unsupervised_heirarchial_MeanShift(df)