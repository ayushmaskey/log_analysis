

def reorganize_data(df, new_list):
	df = df[new_list]
	df = df.reindex(sorted(df.columns), axis = 1)
	return df

def get_training_dataset(df):
	column_list = [col for col in df.columns if col < '2019-02-01']
	df = reorganize_data(df, column_list)
	return df

def get_testing_dataset(df):
	column_list = [col for col in df.columns if col >= '2019-02-01' and col < '2019-03-01']
	df = reorganize_data(df, column_list)
	return df


def get_validation_dataset(df):
	column_list = [col for col in df.columns if col >= '2019-03-01']
	df = reorganize_data(df, column_list)
	return df


def training():
	df_dict = csv_into_dict_of_data()
	
	key_list = list(df_dict.keys())
	for key in key_list:
		df = get_training_dataset(df_dict[key])
		df_dict[key] = df

	return df_dict

def test_new_df_dict():
	df_dict = training()

	key_list = list(df_dict.keys())
	print(key_list)
	for key in key_list:
		print(key, list(df_dict[key].columns))


if __name__ == "__main__":

	test_new_df_dict()