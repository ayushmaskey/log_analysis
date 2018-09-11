from pathlib import Path
from os import stat
import csv
import pandas as pd


def file_exists(fileName):
	path = Path(fileName)
	if not path.is_file():
		open(fileName, 'wb')


def file_empty(fileName):
	is_empty = False
	if stat(fileName).st_size == 0:
		is_empty = True

	return is_empty


def append_to_csv(fileName, df): 
	file_exists(fileName)
	is_empty = file_empty(fileName)

	if is_empty:
		with open(fileName, 'w') as csv_file:
			df.to_csv(csv_file, header = True)
	else:
		with open(fileName, 'a') as csv_file:
			df.to_csv(csv_file, header = False)
