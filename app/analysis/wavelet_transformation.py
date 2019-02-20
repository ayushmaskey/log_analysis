import pandas as pd
import pywt
from pprint import pprint

from csv_to_pandas import csv_into_dict_of_data
from constants import training_dataset


def multi_level_DWT_fxn(data_list, wavelet_to_use, level):
	coeff = pywt.wavedec(data_list, wavelet_to_use, level=level)
	cA = coeff[0]
	# print(cD)
	return cA


def dict_of_df_into_dict_of_dict_of_list(training_dataset):
	df_dict = csv_into_dict_of_data(training_dataset)	
	protocol_list = list(df_dict.keys() )

	# print(df_dict['total']['2018-09-13'].head(5))

	dict_protocol_of_dict_date_of_list_of_data_for_day = {}

	for proto in protocol_list:
		date_list = list(df_dict[proto])

		dict_protocol_of_dict_date_of_list_of_data_for_day[proto] = {}

		for date in date_list:

			proto_date_list = df_dict[proto][date].tolist()

			dict_protocol_of_dict_date_of_list_of_data_for_day[proto][date] = proto_date_list

	return dict_protocol_of_dict_date_of_list_of_data_for_day


def csv_into_wavelet_transformed_dict_of_dataframe(wavelet_to_use, level, csv_path):
	dict_dict_list = dict_of_df_into_dict_of_dict_of_list(csv_path)
	
	# print(dict_dict_list['total']['2018-10-17'])
	for dict_list_key, dict_list_value in dict_dict_list.items():
		for list_key, list_value in dict_dict_list[dict_list_key].items(): 
			
			wavelet_array = multi_level_DWT_fxn(dict_dict_list[dict_list_key][list_key], wavelet_to_use, level)
			wavelet_list = wavelet_array.tolist()
			dict_dict_list[dict_list_key][list_key] = wavelet_list 

			# cA_list = wavelet_fxn(dict_dict_list[dict_list_key][list_key], wavelet_to_use)
			# print(cA_list)
		dict_dict_list[dict_list_key] = pd.DataFrame.from_dict(dict_dict_list[dict_list_key], orient = 'index').transpose()
	return dict_dict_list



def test():
	wavelet_to_use = 'db2'
	level = 1
	dict_dict_list = csv_into_wavelet_transformed_dict_of_dataframe(wavelet_to_use, level, training_dataset)
	from pprint import pprint
	# pprint(dict_dict_list['total'])

	print(list(dict_dict_list))
	test_proto = "total"
	df = dict_dict_list[test_proto]
	df = df.reindex(sorted(df.columns), axis=1)
	print(list(df))



if __name__ == "__main__":

	test()



