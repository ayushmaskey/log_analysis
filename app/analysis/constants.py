

start = 1
end = 10

training_dataset = "../../csv/training_dataset"
testing_dataset = "../../csv/testing_dataset"
validation_dataset = "../../csv/"

plot_save_dir = "../../plots/"

model_save_dir = "../../model/"

wavelet_to_use = ['db1','haar']

label_color_map = {
	0: 'red',	
	1: 'blue',	
	2: 'green',	
	3: 'black',	
	4: 'cyan',	
	5: 'magenta',	
	6: 'yellow',	
	7: 'orange',
	8: 'gold',	
	9: 'salmon',	
	10: 'pink',	
	11: 'grey',	
	12: 'lime',	
	13: 'springgreen',	
	14: 'maroon',	
	15: 'royalblue',
	16: 'brown',	
	17: 'coral',	
	18: 'olive',	
	19: 'lightgreen',	
	20: 'slateblue',	
	21: 'slategray',
	22: 'floralwhite',	
	23: 'darkviolet',
	24: 'plum',	
	25: 'deeppink',
	26: 'crimson',	
	27: 'forestgreen',	
}


k_in_kmeans_before = {
		"date": 
		{
			"conn": 7,
			"dhcp": 2,
			"dns": 6,
			"external": 5,
			"files": 4,
			"http": 6,
			"snmp": 7,
			"total": 5,
			"weird": 7,
		},
		"time": 
		{
			"conn": 6,
			"dhcp": 5,
			"dns": 3,
			"external": 3,
			"files": 2,
			"http": 6,
			"snmp": 7,
			"total": 7,
			"weird": 5,
		}
	}
		# ,
		# "db1": 
		# {
		# 	1: 
		# 	{
		# 		"conn": ,
		# 		"dhcp": ,
		# 		"dns": ,
		# 		"external": ,
		# 		"files": ,
		# 		"http": ,
		# 		"snmp": ,
		# 		"total": ,
		# 		"weird": ,
		# 	}, 
		# 	2: 
		# 	{
		# 		"conn": ,
		# 		"dhcp": ,
		# 		"dns": ,
		# 		"external": ,
		# 		"files": ,
		# 		"http": ,
		# 		"snmp": ,
		# 		"total": ,
		# 		"weird": ,
		# 	}, 
		# 	3: 
		# 	{
		# 		"conn": ,
		# 		"dhcp": ,
		# 		"dns": ,
		# 		"external": ,
		# 		"files": ,
		# 		"http": ,
		# 		"snmp": ,
		# 		"total": ,
		# 		"weird": ,
		# 	}
		# },
		# "haar": 
		# {
		# 	1: 
		# 	{
		# 		"conn": ,
		# 		"dhcp": ,
		# 		"dns": ,
		# 		"external": ,
		# 		"files": ,
		# 		"http": ,
		# 		"snmp": ,
		# 		"total": ,
		# 		"weird": ,
		# 	}, 
		# 	2: 
		# 	{
		# 		"conn": ,
		# 		"dhcp": ,
		# 		"dns": ,
		# 		"external": ,
		# 		"files": ,
		# 		"http": ,
		# 		"snmp": ,
		# 		"total": ,
		# 		"weird": ,
		# 	}, 
		# 	3: 
		# 	{
		# 		"conn": ,
		# 		"dhcp": ,
		# 		"dns": ,
		# 		"external": ,
		# 		"files": ,
		# 		"http": ,
		# 		"snmp": ,
		# 		"total": ,
		# 		"weird": ,
		# 	}
		# }
	# }
