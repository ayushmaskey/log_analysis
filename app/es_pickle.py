from pathlib import Path
from os import stat
import pickle


def pickle_data(fileName, data):
	
	pd_dict = unpickle_data(fileName)

	date = data.index[0].date()
	year = date.year
	month = date.strftime('%B')


	# pd_dict = {year: {month: {date: data} } }
	# pd_dict[date] = data

	print(pd_dict)

	# with open(fileName, 'ab') as pickle_file:
	# 	pickle.dump(pd_dict, pickle_file)
	# 	print(year)


def unpickle_data(fileName):
	file_exists(fileName)
	file_empty(fileName)


	with open(fileName, 'rb') as pickle_file:
		pd_dict = pickle.load(pickle_file)
	return pd_dict


def file_exists(fileName):
	path = Path(fileName)
	if not path.is_file():
		open(fileName, 'wb')


def file_empty(fileName):
	if stat(fileName).st_size == 0:
		pd_dict = {}

		with open(fileName, 'wb') as pickle_file:
			pickle.dump(pd_dict, pickle_file)