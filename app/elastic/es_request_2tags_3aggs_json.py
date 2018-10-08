

def json_internal_to_internal( start, end):
	'''kibana 24hour json'''
	es_request_query = {
		"query": {
		    "bool": {
		      "must": [
		        {
		          "match_all": {}
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
		        {
		          "bool": {
		            "should": [
		              {
		                "term": {
		                  "destination_ip": "192.168.0.0/16"
		                }
		              },
		              {
		                "term": {
		                  "destination_ip": "10.0.0.0/8"
		                }
		              },
		              {
		                "term": {
		                  "destination_ip": "172.16.0.0/12"
		                }
		              }
		            ]
		          }
		        },
		        {
		          "bool": {
		            "should": [
		              {
		                "term": {
		                  "source_ip": "192.168.0.0/16"
		                }
		              },
		              {
		                "term": {
		                  "source_ip": "10.0.0.0/8"
		                }
		              },
		              {
		                "term": {
		                  "source_ip": "172.16.0.0/12"
		                }
		              }
		            ]
		          }
		        }
		      ],
		      "filter": [],
		      "should": [],
		      "must_not": []
		    }
		  }
	    ,
		"size": 0,
		"aggs": {
		    "dest_ip": {
		      "terms": {
		        "field": "dest_ip",
		        # "size": 20000,
		        # "order": {
		        #   "_count": "desc"
		        # }
		      },
		      "aggs": {
		        "dest_port": {
		          "terms": {
		            "field": "dest_port",
		            # "size": 1000,
		          },
		          "aggs": {
		          	"server_name": {
		          		"terms": {
		          			"field": "server_name",
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

def json_internal_to_external( start, end):
	'''kibana 24hour json'''
	es_request_query = {
		"query": {
		    "bool": {
		      "must": [
		        {
		          "match_all": {}
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
		        {
		          "bool": {
		            "must_not": [
		              {
		                "term": {
		                  "destination_ip": "192.168.0.0/16"
		                }
		              },
		              {
		                "term": {
		                  "destination_ip": "10.0.0.0/8"
		                }
		              },
		              {
		                "term": {
		                  "destination_ip": "172.16.0.0/12"
		                }
		              }
		            ]
		          }
		        },
		        {
		          "bool": {
		            "should": [
		              {
		                "term": {
		                  "source_ip": "192.168.0.0/16"
		                }
		              },
		              {
		                "term": {
		                  "source_ip": "10.0.0.0/8"
		                }
		              },
		              {
		                "term": {
		                  "source_ip": "172.16.0.0/12"
		                }
		              }
		            ]
		          }
		        }
		      ],
		      "filter": [],
		      "should": [],
		      "must_not": []
		    }
		  }
	    ,
		"size": 0,
		"aggs": {
		    "dest_ip": {
		      "terms": {
		        "field": "dest_ip",
		        # "size": 20000,
		        # "order": {
		        #   "_count": "desc"
		        # }
		      },
		      "aggs": {
		        "dest_port": {
		          "terms": {
		            "field": "dest_port",
		            # "size": 1000,
		          },
		          "aggs": {
		          	"server_name": {
		          		"terms": {
		          			"field": "server_name",
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
	build_json_query = json_internal_to_internal( start, end)
	print(build_json_query)


 