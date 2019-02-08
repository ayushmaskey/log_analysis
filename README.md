# log_analysis
>elasticsearch network log analysis

---
---
## app

### analysis

#### plot_graph.py
> create 6 level of wavelet transformation and save the graph
```python
import pandas as pd
import matplotlib.pyplot as plt

from csv_to_pandas import dictionary_of_dataframes
from wavelet_transformation import dictOdDictOfList_rawNumber_to_DWTApprox

import sys
sys.path.append('../elastic/')
from es_to_csv import dir_exists, file_exists
```

```python
def wavelet_tranformation_DWT(level):
```
> first plot without any transformation 
* get dictionary of dataframe from csv_to_pandas file using dictionary_of_dataframes function
* no wavelet transformation 
* pass the dataframe to plot_graph_and_save

> then plot wavelet transformed data for the range 1 to level
* get tranformed data from wavelet_transform file using dictOdDictOfList_rawNumber_to_DWTApprox function
* pass each transformed dataframe to plot_graph_save

```python
def plot_graph_and_save(df_dict, identifier):
```
* takes a dictionary of dataframe and id to name the file
* get the keys of dict which is protocols and convert into list
* make sure dictectory to save exists
* for each key in dict which is protocol
* take the value which is dataframe 
* and plot it
* each line in the plot is a column of dataframe which is one day of data.
* remove the legend coz too many days which creates long list of legend
* save the plot in a file

---
---

#### wavelet_transformation.py
> too many transformation between data types: csv, list, dict, dataframe and nest combination of those.

```python
import pandas as pd
import pywt
from pprint import pprint

from csv_to_pandas import dictionary_of_dataframes
```
```python
def dictOdDictOfList_rawNumber_to_DWTApprox(wavelet_to_use, level):
```
* call dictOfDF_into_dictOfProtocol_dictOfDate_listOfTotal to get dict of dict of list
* for loop on each key, value pair of dict of dict of list
* nested for loop for second dict of dict_of_dict_of_list
* pass this list along with wavelet type and level of transformation to call multi_level_DWT_fxn
* multi_level_DWT_fxn return array of cD
* convert this cD array into list and replace the original list
* transform back to dict of combined dataframe
* return this new dict of dataframe which kept its name dict_dict_list making things a little confusing

```python
def multi_level_DWT_fxn(data_list, wavelet_to_use, level):
```
* takes the list for wavelet transformation to given level 
* trasnformation returns cD (detail coeff) and cA (approximation coeff)
* cA discarded??, need to better use this
* array cD returned

```python
def dictOfDF_into_dictOfProtocol_dictOfDate_listOfTotal():
```
* get dictionary of dataframe from csv_to_pandas file using dictionary_of_dataframes function
* get the keys of the dict into a list which is list of protocols
* for each protocol get the dataframe from dict value
* get columns names of that dataframe which is date into a list
* now nested loop, for each date in that list of dates make a dictionary
* dict key: protocol
* dict value: another dict (dict2)
* dict2 key: date
* dict2 value: list of data for the day
* return this dict of dict of list

---
---


#### csv_to_pandas.py
```python
import pandas as pd
import os
import matplotlib.pyplot as plt
```


```python
def dictionary_of_dataframes():
```
* calls get_sub_directories_into_list to get list of dir path and dir
* calls combine_all_csv_to_one_df_per_protcol to get one combined dataframe per protocol
* get combined dataframe for all protocol and make a dictionary
* key of dict: protocol name
* value of dict: combine dataframe for the protocol
* return this massive dict


```python
def combine_all_csv_to_one_df_per_protcol(one_subfolder):
```
* calls get_all_fileNames_inside_folders to get all files in the one_subfolder
* calls make_list_of_dataframe_from_fileNames to get a list of dataframe for files in each subfolder
* takes the list of dataframe and combines into one dataframe
* index is still time of day at 15 minute interval
* each column of dataframe is traffic for the day. 
* column header is the date starting from 8-30-18 to today
* return the combined dataframe

```python
def make_list_of_dataframe_from_fileNames(files_with_path):
```
* calls make_dataframe_from_csv to  convert data of each files into dataframe
* does the same for all files in that folder and appends them all to a list

```python
def make_dataframe_from_csv(file):
```
* get the csv file from the input file with full path name
* convert into dataframe with time as index and total traffic as column

```python
def get_all_fileNames_inside_folders(one_subfolder):
```
* returns all the file inside the folder
* all files in full pathname starting from root of the project

```python
def get_sub_directories_into_list(path):
```
* traverses through csv folder to get sub folders 
* returns a list of directory path and list of directory
---
---




### elastic

```python
python3 -m doctest -v es_connection.py
```
#### elastic.cron

* load_daily.py every morning
* git add, commit and push after 10 min
* generates log for run and git in elastic.log
```bash
crontab -e 			#edit
crontab -l			#view
crontab elastic.cron 		#add new cron job
```
---

#### load_one_time.py
* run last 17 days on es_traffic_pandas_csv as a one time thing for all protocol
* the function called returns pandas dataframe.
* something was probably changed and for load_daily but not load_one_time probably not updated
* ???
```python
def push_to_csv
```
---

#### load_daily.py
* get single level indices from es_index_fileName
* call es_traffic_pandas_csv to get dataframe
* call append_to_csv to append data into csv
```python
def es_simple_agg
```

* aggregate websites visited --* sounds important
* not used
* ???
* calls threeAggs_2Tags which returns a dict of list
* each pair is ignored and es_nested_agg_pandas is called with variable not defined or imported. but it is a know  function in different file to build json
* very confused where i was going with this
* maybe I was testing higher order function by passing a function in a function
* I probably didn't need it but I was probably reading about function that takes function as parameter
* es_nested_agg_pandas returns dataframe which is appended to csv files
```python
def es_3agg_2tag_agg
```
---

#### es_index_fileName
* single level has simple indexes, like total, dns, dhcp etc
* threeAggs - not sure
```python
def single_level_query
def threeAggs_2Tags
```
---

#### es_pandas.py
> strip complex url to get domain name
```python
import es_connection, es_request_json, es_pickle
def domain_name(str):
	return domain name like google.com
```
* uses simple json structure in aggStructure to flatten 3 level nested aggs response from elastic
* found online 
* complex elastic result to df
* and to top it off it is recursive. I definitely didn't write this function 
```python
def elasticAggsToDataframe(elasticResult,aggStructure,record={},fulllist=[]):
	flatten nested aggs response from elastic: stackoverflow
```
> convert elastic data to pandas dataframe
```python
def get_pandas_dataframe(ind, start, end):
	return es_agg_converted_to_panda_dataframe
```
> build json query,connect to elastic, retrieve data, get the aggs and pass to get_pandas_dataframe
```python
def es_traffic_pandas_csv(fileName, ind, start, end):
```
* uses function from parameter fn_for_json_query to build json query
* connect to elasticsearch pull the data using that json
* calls elasticAggsToDataframe to flatted elastic response to df
* strip to domain name if it is external server
* strip to server name if it is internal server
* encrypt the IP using SHA1
* drop duplicates
* return the dataframe
```python
def es_nested_agg_pandas(start, end, fn_for_json_query, traffic_type):
```
> can't find this function
```python

def get_agg_response_list_of_dict(ind, start, end ):
	return agg_es_data_15min_interval
```

---
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
---
#### es_request_protocol_json.py
* build json query for protocols different than total
* index = {dns, dhcp...}
```python
def json_protocol_query(index, startDate, endDate):
	return json_structure_ready_for_es_query
```
---

#### es_request_external_json.py
* build json query for traffic between internal source to external destination
* what is the difference from  json_internal_to_external in es_request_2tags_3aggs_json ??
```python
def json_external_query
	return es_request_query
```
---

#### es_request_2tags_3aggs_json
* build json query for internal source to internal destination --* traffic within the network
* build json query for internal source to external destination --> traffic going out
```python
def json_internal_to_internal
def json_internal_to_external
```
---

#### es_aggregate_structure_json
> simple json structure used to break down complex, multiple aggs level data simple df
```python
def agg_firewall_external_dest
```
---


#### es_to_csv.py
```python
def dir_exists(dirName):
def file_exists(fileName):
def file_empty(fileName):
def line_count_97(fileName):
def build_directory(fileName):
```
* creates file path, checks if directory and file exists, 
* check if file is empty but not used ??
* verify 97 lines in csv, if not rewite the file
* 97 lines represent 96 traffic data and 1 header
```python
def append_to_csv(fileName, df):
```
* not used coz it has to be used with that complicated firewal thing that is on hold
* similar to append_to_csv but actually uses result of check of file is empty
```python
def append_nested_aggs_to_csv(fileName, df):
```
---
---

## log

#### elastic.log
> log of all activity inluding git and running script
