# log_analysis
elasticsearch network log analysis

## app

### elastic

#### es_connection.py
> connect to elastic
```python
def es_connect():
	return es_client_connection

```

---

#### es_request_total_json.py
> build json for total traffic with index = *
```python
def json_query(index, startDate, endDate):
	return json_structure_ready_for_es_query
```

#### es_request_protocol_json.py
Json query for protocols different than total
index = {dns, dhcp...}
```python
def json_protocol_query(index, startDate, endDate):
	return json_structure_ready_for_es_query
```


#### es_pandas.py
```python
import es_connection, es_request_json, es_pickle

def domain_name(str):
	return domain name like google.com

def elasticAggsToDataframe(elasticResult,aggStructure,record={},fulllist=[]):
	flatten nested aggs response from elastic: stackoverflow

def get_pandas_dataframe(ind, start, end):
	return es_agg_converted_to_panda_dataframe


def get_agg_response_list_of_dict(ind, start, end ):
	return agg_es_data_15min_interval



def es_traffic_pandas_csv(fileName, ind, start, end):
	manages_es_request_panda_conversion_load_csv

```

#### es_to_csv.py
```python


```

#### load_one_time.py
```python


```

#### load_daily.py
```python


```

#### elastic.cron

run load_daily.py every morning
git add, commit and push after 10 min


```bash
crontab -e 			#edit
crontab -l			#view
crontab elastic.cron 		#add new cron job
```
