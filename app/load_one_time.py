from es_pandas import es_traffic_pandas_csv


def push_to_csv(ind):
	for i in range(1,17):
		
		start = "now-"+str(i)+"d"
		end = "now"

		csv_file_path = '../csv/'
		csv_file_name = 'total.csv'
		fileName = csv_file_path + csv_file_name
		
		es_traffic_pandas_csv(fileName, ind, start, end)

if __name__ == "__main__":
	ind = {
			"total": "*", 
			"dhcp": "event_type:bro_dhcp",
			"dns": "event_type:bro_dns",
			"conn": "event_type:bro_conn",
			"snmp": "event_type:bro_snmp",
			"weird": "event_type:bro_weird",
			"http": "event_type:bro_http",
			"files": "event_type:bro_files",
		}
	push_to_csv(ind['total'])
	# print(ind["dhcp"])