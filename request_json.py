def total_traffic_count_15m_interval():
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
		      "gte": "now-7d",
		      "lte": "now",
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
		                  "gte": "now-24H",
		                  "lte": "now",
		                  "format": "epoch_millis"
		                }
		              }
		            }
		         ],
		          "must_not": []
		        }
		      }
		    }
		  },
		  "size": 0,
		  "aggs": {
		    "top_10_ip": {
		      "terms": {
		        "field": "ips",
		        "size": 10,
		        "order": {
		          "_count": "desc"
		        }
		      }
		    }
		  }
		}
	return body

def list_field_names():
	body={
		"aggs": {
			"Field names": {
				"terms": "_field_names",
				"size": 10
			}
		}
	}
