#!/usr/bin/python3

import datetime as dt

import es_pandas 
import es_to_csv
import es_index_fileName

#function to run all timeseries histogram with 1 aggs and save to csv
def es_simple_agg(start, end):
	ind = es_index_fileName.single_level_query()

	for key, value in ind.items():
		fileName = key
		ind = value
		df = es_pandas.es_traffic_pandas_csv(ind, start, end)
		es_to_csv.append_to_csv(fileName, df)


#function to run nested aggs and save to csv --> 3aggs and 2 tags
def es_3agg_2tag_agg(start, end):
	ind = es_index_fileName.threeAggs_2Tags()

	for key, value in ind.items():
		fileName = key
		df = es_pandas.es_nested_agg_pandas(start, end, json_internal_to_internal)
		es_to_csv.append_nested_aggs_to_csv(fileName, df)

# sample printout to remind myself whats up
def sample_es_simple_agg():
	ind = es_index_fileName.single_level_query()

	start = "now-1d"
	end = "now"

	print(ind)
	ind = "bro_dhcp"
	df = es_pandas.es_traffic_pandas_csv(ind, start, end)
	print(df)

#main function to load data --> set up run automatically using cron job
def load_main():
	start = "now-3d"
	end = "now"

	es_simple_agg(start, end)
	# es_3agg_2tag_agg(start, end)

	print("daily load on", dt.datetime.now() ,"successful!!")


if __name__ == "__main__":
	load_main()

	# sample_es_simple_agg()

