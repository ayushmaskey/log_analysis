
def getDuplicateColumns(df):
	'''
	Get a list of duplicate columns.
	It will iterate over all the columns in dataframe and find the columns whose contents are duplicate.
	:param df: Dataframe object
	:return: List of columns whose contents are duplicates.
	'''
	duplicateColumnNames = set()
	# Iterate over all the columns in dataframe
	for x in range(df.shape[1]):
		# Select column at xth index.
		col = df.iloc[:, x]
		# Iterate over all the columns in DataFrame from (x+1)th index till end
		for y in range(x + 1, df.shape[1]):
			# Select column at yth index.
			otherCol = df.iloc[:, y]
			# Check if two columns at x 7 y index are equal
			if col.equals(otherCol):
				duplicateColumnNames.add(df.columns.values[y])
	return list(duplicateColumnNames)