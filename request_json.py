def sample_json1():
	'''kibana 24hour json'''
	body = {
		"query": {
		 "bool": {
		  "must": [
		   {
		    "query_string": {
		     "query": "*",
		     "analyze_wildcard": "true"
		    }
		   },
		   {
		    "range": {
		     "@timestamp": {
		      "gte": "1521353712139",
		      "lte": "1521440112139",
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
		 "tag_name": {
		  "date_histogram": {
		   "field": "@timestamp",
		   "interval": "30m",
		   "time_zone": "Pacific/Honolulu",
		   "min_doc_count": 1
		  }
		 }
		} 
	}
	return body

def sample_json2():
	'''json from qbox example'''
	body = {
		"query": {
		 "filtered": {
		  "query": {
		   "query_string": {
		    "query": "*",
		    "analyze_wildcard": "true"
		   }
		  },
		  "filter": {
		   "bool": {
		    "must": [
		     {
		      "range": {
		       "@timestamp": {
		        "gte": "now-12M",
		        "lte": "now",
		        "format": "epoch_millis"
		       }
		      }
		     }
		    ],
		    "must_not":[]
		   }
		  }
		 }
		},
		"size": 0,
		"aggs": {
		 "tag_name": {
		  "terms": {
		   "field": "remote_ip.raw",
		   "size": 1000,
		   "order": {
		    "_count": "desc"
		   }
		  }
		 }
		}
	}
	return body