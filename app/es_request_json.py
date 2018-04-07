
def total_traffic(query_filter, start, end):
	'''kibana 24hour json'''
	body = {
		"query": {
		 "bool": {
		  "must": [
		   {
		    "query_string": {
		     "query": query_filter,
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
		   }
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
	return body