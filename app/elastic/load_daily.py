#!/usr/bin/python3

from es_pandas import es_traffic_pandas_csv


def push_to_csv(fileName, index):
		start = "now-2d"
		end = "now"

		es_traffic_pandas_csv(fileName, index, start, end)

if __name__ == "__main__":
	ind = {
			"total": "*", 
			"dhcp": "bro_dhcp",
			"dns": "bro_dns",
			"conn": "bro_conn",
			"snmp": "bro_snmp",
			"weird": "bro_weird",
			"http": "bro_http",
			"files": "bro_files",
		}


	for key, value in ind.items():
		push_to_csv(key, value)
