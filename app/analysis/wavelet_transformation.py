import pandas as pd
import pywt
from pprint import pprint

from csv_to_pandas import dictionary_of_dataframes

def multi_level_DWT_fxn(data_list, wavelet_to_use, level):
	coeff = pywt.wavedec(data_list, wavelet_to_use, level=level)
	cD = coeff[0]
	# print(cD)
	return cD


def dictOfDF_into_dictOfProtocol_dictOfDate_listOfTotal():
	df_dict = dictionary_of_dataframes()	
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


def dictOfDictOfList_rawNumber_to_DWTApprox(wavelet_to_use, level):
	dict_dict_list = dictOfDF_into_dictOfProtocol_dictOfDate_listOfTotal()
	
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
	wavelet_to_use = 'db1'
	level = 1
	dict_dict_list = dictOfDF_into_dictOfProtocol_dictOfDate_listOfTotal()
	from pprint import pprint
	pprint(dict_dict_list['total'])
	# wavelet_array = multi_level_DWT_fxn(dict_dict_list['total']['2018-10-19'], wavelet_to_use, level)


	# dictOdDictOfList_rawNumber_to_DWTApprox(multi_level_DWT_fxn, wavelet_to_use, 1)
	# print("\n\r\n\r\n\r")
	# wavelet_array = single_level_DWT_fxn(dict_dict_list['total']['2018-10-19'], wavelet_to_use, level)
	# dictOdDictOfList_rawNumber_to_DWTApprox(single_level_DWT_fxn, wavelet_to_use, 1)



if __name__ == "__main__":

	test()



