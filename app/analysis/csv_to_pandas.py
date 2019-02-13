import pandas as pd
import os
import matplotlib.pyplot as plt

def get_sub_directories_into_list(path):
	dir_list = os.listdir(path)
	dir_list.remove('test')
	dir_path_list = [path + '/{0}'.format(dirs) for dirs in dir_list ]
	
	return dir_path_list, dir_list


def make_dataframe_from_csv(file):
	df = pd.read_csv(file, index_col = 0)
	
	col = df.Date[0]
	df = df.rename(columns = {"Total": col})
	df = df.drop(['Date'], axis = 1)

	return df


def get_all_fileNames_inside_folders(one_subfolder):
	files = os.listdir(one_subfolder)
	files_with_path = [one_subfolder + '/{0}'.format(file) for file in files]
	
	return files_with_path


def make_list_of_dataframe_from_fileNames(files_with_path):
	df_list = []

	for file in files_with_path:
		df_list.append( make_dataframe_from_csv(file) )

	return df_list


def combine_all_csv_to_one_df_per_protcol(one_subfolder):

	files_with_path = get_all_fileNames_inside_folders(one_subfolder)
	df_list = make_list_of_dataframe_from_fileNames(files_with_path)

	i = 0

	df_combined = df_list[i] 
	for i in range(1, len(df_list)):
		df_combined = pd.concat([df_combined, df_list[i]], axis = 1, sort=True)
 		

	df_combined.fillna(0, inplace = True)
	
	return df_combined


def csv_into_dict_of_data():
	csv_path = "../../csv"
	dir_path_list, dir_list = get_sub_directories_into_list(csv_path)
		
	df_dict = {}

	for i in range(0, len(dir_path_list)):
		df_dict[dir_list[i]] = combine_all_csv_to_one_df_per_protcol(dir_path_list[i])


	return df_dict




def test():
	csv_path = "../../csv"
	one_folder = csv_path + "/total/"
	one_file = one_folder + "total_2018-10-12.csv"

	dir_path, dir_list = get_sub_directories_into_list(csv_path)
	# print(dir_path)

	files = get_all_fileNames_inside_folders(dir_path[0])
	# print(files)

	one_df = make_dataframe_from_csv(one_file)
	# print(one_df.head(5))

	df_list = make_list_of_dataframe_from_fileNames(files)
	# print(df_list)

	df_csv = combine_all_csv_to_one_df_per_protcol(one_folder)
	# print(df_csv.head(5))

	# df = dictionary_of_dataframes(csv_path)
	# print(df)

if __name__ == "__main__":

	# test()

	# print dataframe with column names sorted alphabetically 
	df = combine_all_csv_to_one_df_per_protcol('../../csv/total')
	df = df.reindex(sorted(x.columns), axis=1)
	print(df)