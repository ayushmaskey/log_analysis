

def agg_firewall_external_dest():
	aggStructure = [
			{'key':'dest_ip',
			'aggs':[
				{'key':'dest_port',
				'aggs':[
					{'key':'server_name',
					'variables':[
						{'elasticName':'doc_count',
						'dfName':'Count'
						}
					]
					}
				]
				}
			]
			}
		]
	return aggStructure

