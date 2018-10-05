

def json_firewall_outside_query(index, start, end):
	'''kibana 24hour json'''
	es_request_query = {
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
	    },
		"size": 0,
		"aggs": {
		    "dest_ip": {
		      "terms": {
		        "field": "destination_ips.keyword",
		        # "size": 100000,
		        # "order": {
		        #   "_count": "desc"
		        # }
		      },
		      "aggs": {
		        "dest_port": {
		          "terms": {
		            "field": "destination_port",
		            # "size": 100000,
		          #   "order": {
		          #     "_count": "desc"
		          #   }
		          },
		          "aggs": {
		          	"server_name": {
		          		"terms": {
		          			"field": "server_name.keyword",
		          		}
		          	}
		          }
		        }
		      }
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
	build_json_query = json_firewall_outside_query(ind, start, end)
	print(build_json_query)


 