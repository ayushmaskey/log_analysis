
def json_query(index, start, end):
	'''kibana 24hour json'''
	es_request_query = {
		"query": {
		 "bool": {
		  "must": [
		   {
		    "query_string": {
		     "query": index,
		     "analyze_wildcard": "true"
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
		   },
		  ],
		  "must_not": []
		 }
		},
		"size": 0,
		"aggs": {
		 "total_traffic": {
		  "date_histogram": {
		   "field": "@timestamp",
		   "interval": "15m",
		   "time_zone": "Pacific/Honolulu",
		   "min_doc_count": 1
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
	build_json_query = json_query(ind, start, end)
	print(build_json_query)


