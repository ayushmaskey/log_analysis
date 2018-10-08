
def single_level_query():
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
	return ind

def threeAggs_2Tags():
	ind = {
		"external_dst": [
			"destination_ips.keyword",
			 "destination_port",
			 "server_name.keyword",
			 "external_destination",
			 "internal_source"
		],
		# "internal_dst": [
		# 	"destination_ips.keyword",
		# 	 "destination_port",
		# 	 "server_name.keyword",
		# 	 "internal_destination",
		# 	 "internal_source"
		# ]
	}
	return ind