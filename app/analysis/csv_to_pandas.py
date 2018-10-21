import pandas as pd
import os
import matplotlib.pyplot as plt

def made_dataframe_from_csv(file):
	df = pd.read_csv(file, index_col = 0)
	
	col = df.Date[0]
	df = df.rename(columns = {"Total": col})
	df = df.drop(['Date'], axis = 1)

	return df




def get_fileNames_inside_subfolders(dirs):
	files = os.listdir(dirs)

	files_with_path = [dirs + '/{0}'.format(file) for file in files]

	i = 0
	df = []

	for file in files_with_path:
		df.append( made_dataframe_from_csv(file) )


	df_final = df[0] 
	for i in range(1, len(df)):
		df_final = pd.concat([df_final, df[i]], axis = 1)
 		

	df_final.fillna(0, inplace = True)
	
	return df_final
	

def loop_over_directory_structure_return_pandas_df(csv_path):
	dir_list = os.listdir(csv_path)
	dir_list.remove('test')

	
	dir_path_list = [csv_path + '/{0}'.format(dirs) for dirs in dir_list ]
	
	df_dict = {}

	for i in range(0, len(dir_path_list)):
		df_dict[dir_list[i]] = get_fileNames_inside_subfolders(dir_path_list[i])

	# print(df_dict)


	return df_dict




def test():
	csv_path = "../../csv"
	loop_over_directory_structure_return_pandas_df(csv_path)





if __name__ == "__main__":

	test()