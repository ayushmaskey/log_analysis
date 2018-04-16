import pickle


def pickle_data(fileName, data):
	
	db = {}

	date = data.index[0].date()
	year = date.year
	month = date.strftime('%B')


	# db = {year: {month: {date: data} } }
	db[date] = data

	with open(fileName, 'ab') as pickle_file:
		pickle.dump(db, pickle_file)


def unpickle_data(fileName):
	
	with open(fileName, 'rb') as pickle_file:
		pd_dict = pickle.load(pickle_file)
	return pd_dict


