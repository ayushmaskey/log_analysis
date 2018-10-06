#!/usr/bin/python3

import datetime as dt

from es_pandas import es_traffic_pandas_csv
from es_to_csv import append_to_csv


def es_simple_agg(start, end):
	ind = {
			"total": "*", 
			"dhcp": "bro_dhcp",
			"dns": "bro_dns",
			"conn": "bro_conn",
			"snmp": "bro_snmp",
			"weird": "bro_weird",
			"http": "bro_http",
			"files": "bro_files",
			"external": "external"
		}

	for key, value in ind.items():
		fileName = key
		ind = value
		df = es_traffic_pandas_csv(ind, start, end)
		append_to_csv(fileName, df)


def load_main():
	start = "now-2d"
	end = "now"

	es_simple_agg(start, end)
	print("daily load on", dt.datetime.now() ,"successful!!")


if __name__ == "__main__":
	load_main()