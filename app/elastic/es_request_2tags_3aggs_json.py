

def json_three_level_agg_query_two_tags( start, end, agg1, agg2, agg3, tag1, tag2):
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
	              "query": tag1
	            }
	          }
	        },
	        {
	          "match_phrase": {
	            "tags": {
	              "query": tag2
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
		        "field": agg1,
		        # "size": 20000,
		        # "order": {
		        #   "_count": "desc"
		        # }
		      },
		      "aggs": {
		        "dest_port": {
		          "terms": {
		            "field": agg2,
		            # "size": 1000,
		          },
		          "aggs": {
		          	"server_name": {
		          		"terms": {
		          			"field": agg3,
		            		# "size": 1000,

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


 