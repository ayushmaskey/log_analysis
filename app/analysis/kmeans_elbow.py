import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans, MeanShift
from constants import start, end, training_dataset
from csv_to_pandas import csv_into_dict_of_data


# fnding elbow
def find_k_for_KMeans_elbow_method_sum_of_square_to_nearest_centroid(df):
	distortions = []
	for k in range(start, end):
		km = KMeans(n_clusters = k)
		km.fit(df)
		distortions.append(km.inertia_)
	return distortions

def find_k_for_KMeans_elbow_method_score(df):
	Nc = range(start, end)

	km = [KMeans(n_clusters=i) for i in Nc]
	score = [km[i].fit(df).score(df) for i in range(len(km))]
	return score

def plot_elbow(score):
	# Plot the elbow
	fig = plt.figure(figsize=(15, 5))
	plt.plot(range(start, end), score)
	# plt.xlabel('Number of Clusters')
	# plt.ylabel('Score')
	plt.grid(True)
	plt.title('Elbow Method to find k using inertia_')
	plt.show()

if __name__ == "__main__":

	df_dict = csv_into_dict_of_data(training_dataset)
	key_list = list(df_dict.keys())


	df = df_dict['snmp']
	score = find_k_for_KMeans_elbow_method_score(df)
	print(score)
	plot_elbow(score)

	distortions = find_k_for_KMeans_elbow_method_sum_of_square_to_nearest_centroid(df)
	print(distortions)
	plot_elbow(distortions)

