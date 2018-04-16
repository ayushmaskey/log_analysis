# log_analysis
elasticsearch network log analysis

## app

#### es_connection.py
```python
def es_connect():
	return es_client_connection

def db_connect():
	if_i_use_sqlite3
```

#### es_request_json.py
```python
def json_query(index, startDate, endDate):
	return json_structure_ready_for_es_query
```

#### es_pickle.py
```python
def file_existe(fileName):
	create_new_file_if_not_exisits

def file_empty(fileName):
	create_empty_dict_if_empty

def pickle_data(fileName:
	add_new_pickled_pandas_dataFrame_dict

def unpickle_data(fileName:
	return pickled_pandas_dataFrame_dict
```

#### pickled data structure
```python
option 1: {year(int): {'monthName'(str): {'date'(date): {panda_dataframe_for_the_day} } } }
option 2: {'date'(date): {panda_dataframe_for_the_day} }

panda_dataframe_for_the_day [TimeSeriesIndex | total_traffic_count | unix_time ]

option 2 for now since it is simple but maybe difficult to manage when years of data collected
```

#### es_pandas.py
```python
import es_connection, es_request_json, es_pickle

def get_agg_response_list_of_dict(ind, start, end ):
	return agg_es_data_15min_interval

def get_pandas_dataframe(ind, start, end):
	return es_agg_converted_to_panda_dataframe

def es_traffic_pandas_pickle(fileName, ind, start, end):
	manages_es_request_panda_conversion_load_pickle

```