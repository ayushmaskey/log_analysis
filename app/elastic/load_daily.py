#!/usr/bin/python3

import datetime as dt

from es_pandas import es_traffic_pandas_csv
from es_pandas import es_nested_agg_pandas

from es_to_csv import append_to_csv
from es_to_csv import append_nested_aggs_to_csv

from es_index_fileName import single_level_query
from es_index_fileName import threeAggs_2Tags

#function to run all timeseries histogram with 1 aggs and save to csv
def es_simple_agg(start, end):
	ind = single_level_query()

	for key, value in ind.items():
		fileName = key
		ind = value
		df = es_traffic_pandas_csv(ind, start, end)
		append_to_csv(fileName, df)


#function to run nested aggs and save to csv --> 3aggs and 2 tags
def es_3agg_2tag_agg(start, end):
	ind = threeAggs_2Tags()

	for key, value in ind.items():
		fileName = key
		df = es_nested_agg_pandas(start, end, value[0], value[1], value[2], value[3], value[4])
		append_nested_aggs_to_csv(fileName, df)


#main function to load data --> set up run automatically using cron job
def load_main():
	start = "now-2d"
	end = "now"

	es_simple_agg(start, end)
	# es_3agg_2tag_agg(start, end)

	print("daily load on", dt.datetime.now() ,"successful!!")


if __name__ == "__main__":
	load_main()