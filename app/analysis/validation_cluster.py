import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

from csv_to_pandas import csv_into_dict_of_data
from wavelet_transformation import csv_into_wavelet_transformed_dict_of_dataframe

from training_cluster import reorganize_data

def get_validation_dataset(df):
	column_list = [col for col in df.columns if col >= '2019-03-01']
	df = reorganize_data(df, column_list)
	return df


def vaidation():
	df_dict = csv_into_dict_of_data()
	
	key_list = list(df_dict.keys())
	for key in key_list:
		df = get_validation_dataset(df_dict[key])
		df_dict[key] = df

	return df_dict

def test_new_df_dict():
	df_dict = vaidation()

	key_list = list(df_dict.keys())
	print(key_list)
	for key in key_list:
		print(key, list(df_dict[key].columns))


if __name__ == "__main__":

	test_new_df_dict()