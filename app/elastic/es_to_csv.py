from pathlib import Path
from os import stat
import csv
import pandas as pd


def dir_exists(dirName):
	"""check if directory exists, if not create the directory"""
	path = Path(dirName)
	if not Path(dirName).is_dir():
		Path(dirName).mkdir()
	return Path(dirName).is_dir()

def file_exists(fileName):
	"""	check if file exists, if not create the file"""
	path = Path(fileName)
	if not path.is_file():
		open(fileName, 'wb')
	return Path(fileName).is_file()


def file_empty(fileName):
	"""check if file is empty"""
	is_empty = False
	if stat(fileName).st_size == 0:
		is_empty = True
	return is_empty

def line_count_97(fileName):
	"""Check if file has 97 rows
	1 row for header 
	96 row for doc count every 15 min - 24hour * 4 per hour
	"""
	with open(fileName) as csv_file:
		spamreader = csv.reader(csv_file)
		row_count = sum(1 for row in spamreader)
	return row_count == 97

def build_directory(fileName):
	"""construnct full path of for the file"""
	csv_file_path = '/home/amaskey/Documents/log_analysis/csv/'
	dirName = csv_file_path + fileName
	return dirName
	
def append_to_csv(fileName, df):
	"""check if the file and directory exists, create one if needed
		files named by protocol and date
		if the file has 97 lines, no need to update file for that day.
		if not less than 97 rows, delete everything and write new data in csv for that day
	"""
	dirName = build_directory(fileName)
	csv_ext = '.csv'

	unique_dates = df['Date'].unique()

	for unique_date in unique_dates:
		date_str = str(unique_date) 
		full_path = dirName + "/" + fileName + '_' + date_str + csv_ext

		new_df = df[df['Date'] == unique_date]

		if dir_exists(dirName) and file_exists(full_path):

			is_empty = file_empty(full_path)

			if not line_count_97(full_path):
				with open(full_path, 'w') as csv_file:
					new_df.to_csv(csv_file, header = True)
	
def append_nested_aggs_to_csv(fileName, df):
	"""check if the file and directory exists, create one if needed
		if the file is empty, write data to csv
		if the file is not empty, concat new and old dataframe and remove duplicates
	"""
	dirName = build_directory(fileName)
	csv_ext = '.csv'

	full_path = dirName + "/" + fileName + csv_ext

	if dir_exists(dirName) and file_exists(full_path):

			is_empty = file_empty(full_path)

			if not is_empty:
				with open(full_path, 'r') as csv_file:
					old_df = pd.read_csv(full_path)

				if not old_df.empty:
					old_df.index = old_df['sha1']
					old_df = old_df[["dest_ip", "dest_port", "URL"]]
					new_df = pd.concat([df, old_df])
					new_df.drop_duplicates(keep = 'first', inplace=True)
					# print(new_df)
			else:
				new_df = df	


			with open(full_path, 'w') as csv_file:
					new_df.to_csv(csv_file, header = True)

