from es_pandas import es_traffic_pandas_csv


def push_to_csv(ind):
		start = "now-2d"
		end = "now"

		fileName, index = ind

		es_traffic_pandas_csv(fileName, index, start, end)

if __name__ == "__main__":
	ind = {
			"total": ["total","*"], 
			"dhcp": "event_type:bro_dhcp",
			"dns": "event_type:bro_dns",
			"conn": "event_type:bro_conn",
			"snmp": "event_type:bro_snmp",
			"weird": "event_type:bro_weird",
			"http": "event_type:bro_http",
			"files": "event_type:bro_files",
		}
	push_to_csv(ind['total'])
