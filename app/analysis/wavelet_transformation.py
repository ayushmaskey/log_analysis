import pandas as pd
import pywt
from pprint import pprint

from csv_to_pandas import dictionary_of_dataframes


def single_level_discrete_wavelet_transform(data_list):
	(cA, cD) = pywt.dwt(data_list, 'db1')
	print(cA)
	print(cD)

def dictOfDF_into_dictOfProtocol_dictOfDate_listOfTotal():
	df_dict = dictionary_of_dataframes()	
	protocol_list = list(df_dict.keys() )

	# print(df_dict['total']['2018-09-13'].head(5))

	dict_protocol_with_nested_list_each_nested_list_is_a_day = {}

	for proto in protocol_list:
		date_list = list(df_dict[proto])

		dict_protocol_with_nested_list_each_nested_list_is_a_day[proto] = {}

		for date in date_list:
			dict_key = proto + "_" + date

			proto_date_list = df_dict[proto][date].tolist()

			dict_protocol_with_nested_list_each_nested_list_is_a_day[proto][date] = proto_date_list

	return dict_protocol_with_nested_list_each_nested_list_is_a_day



def somethin():
	dict_dict_list = dictOfDF_into_dictOfProtocol_dictOfDate_listOfTotal()
	# pprint(x['total']['2018-10-18'])
	
	for dict_list_key, dict_list_value in dict_dict_list.items():
		for list_key, list_value in dict_dict_list[dict_list_key].items(): 
			print(dict_list_key,list_key)

def test():
	somethin()



if __name__ == "__main__":

	test()



