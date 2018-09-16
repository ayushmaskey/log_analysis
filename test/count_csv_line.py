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



def append_to_csv(fileName, df):

	csv_file_path = '../csv/'
	csv_ext = '.csv'
	dirName = csv_file_path + fileName

	unique_dates = df['Date'].unique()

	for unique_date in unique_dates:
		date_str = str(unique_date) 
		fileName_date = dirName + "/" + fileName + '_' + date_str + csv_ext

		new_df = df[df['Date'] == unique_date]

		if dir_exists(dirName) and file_exists(fileName_date):

			is_empty = file_empty(fileName_date)

			# if is_empty:
			with open(fileName_date, 'w') as csv_file:
				new_df.to_csv(csv_file, header = True)
			# else:
			# 	with open(fileName_date, 'a') as csv_file:
			# 		new_df.to_csv(csv_file, header = False)
	

def line_count_97(fileName):
	with open(fileName) as csv_file:
		spamreader = csv.reader(csv_file)
		row_count = sum(1 for row in spamreader)
	print(row_count)
	return row_count == 97

if __name__ == "__main__":

	fileName1 = "../csv/total/total_2018-09-10.csv"
	fileName2 = "../csv/total/total_2018-09-13.csv"
	fileName3 = "../csv/total/total_2018-09-14.csv"
	fileName4 = "../csv/total/total_2018-09-15.csv"


	print(line_count_97(fileName1))
	print(line_count_97(fileName2))
	print(line_count_97(fileName3))
	print(line_count_97(fileName4))