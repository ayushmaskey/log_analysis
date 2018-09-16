# log_analysis
elasticsearch network log analysis

## app

#### es_connection.py
```python
def es_connect():
	return es_client_connection

def db_connect():
	if_I_use_sqlite3_or_any_other_Db
```

#### es_request_total_json.py
```python
def json_query(index, startDate, endDate):
	return json_structure_ready_for_es_query
```

#### es_request_protocol_json.py
Json query for protocols different than total
```python
def json_protocol_query(index, startDate, endDate):
	return json_structure_ready_for_es_query
```


#### es_pandas.py
```python
import es_connection, es_request_json, es_pickle

def get_agg_response_list_of_dict(ind, start, end ):
	return agg_es_data_15min_interval

def get_pandas_dataframe(ind, start, end):
	return es_agg_converted_to_panda_dataframe

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
