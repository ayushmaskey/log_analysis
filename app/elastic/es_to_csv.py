from pathlib import Path
from os import stat
import csv
import pandas as pd


def dir_exists(dirName):
	path = Path(dirName)
	if not Path(dirName).is_dir():
		Path(dirName).mkdir()
	return Path(dirName).is_dir()

def file_exists(fileName):
	path = Path(fileName)
	if not path.is_file():
		open(fileName, 'wb')
	return Path(fileName).is_file()


def file_empty(fileName):
	is_empty = False
	if stat(fileName).st_size == 0:
		is_empty = True

	return is_empty

def line_count_97(fileName):
	with open(fileName) as csv_file:
		spamreader = csv.reader(csv_file)
		row_count = sum(1 for row in spamreader)
	return row_count == 97

def append_to_csv(fileName, df):

	csv_file_path = '/home/amaskey/Documents/log_analysis/csv/'
	csv_ext = '.csv'
	dirName = csv_file_path + fileName

	unique_dates = df['Date'].unique()

	for unique_date in unique_dates:
		date_str = str(unique_date) 
		fileName_date = dirName + "/" + fileName + '_' + date_str + csv_ext

		new_df = df[df['Date'] == unique_date]

		if dir_exists(dirName) and file_exists(fileName_date):

			is_empty = file_empty(fileName_date)

			if not line_count_97(fileName_date):
				with open(fileName_date, 'w') as csv_file:
					new_df.to_csv(csv_file, header = True)
	
