

def json_external_query(index, start, end):
	'''kibana 24hour json'''
	es_request_query = {
		"_source" : ["@timestamp", "source_ips", "destination_ips", "destination_port"],
		"query": {
		    "bool": {
		      "must": [
		        {
		          "match_all": {}
		        },
		        {
		          "match_phrase": {
		            "tags": {
		              "query": "external_destination"
		            }
		          }
		        },
		        {
		          "match_phrase": {
		            "tags": {
		              "query": "internal_source"
		            }
		          }
		        },
		        {
		          "range": {
		            "@timestamp": {
		              "gte": start,
		              "lte": end,
		              "format": "epoch_millis"
		            }
		          }
		        }
		      ],
		      "filter": [],
		      "should": [],
		      "must_not": []
		    }
	    } 
	}
	return es_request_query







if __name__ == "__main__":
	ind = "*"
	start = "now-1d"
	end = "now"
	tag1 = "*"
	tag2 = "*"
	build_json_query = json_external_query(ind, start, end)
	print(build_json_query)


 