
from es_pandas import get_pandas_datafrane

ind = "*"
start = "now-1d"
end = "now"


if __name__ == "__main__":
	df = get_pandas_datafrane(ind, start, end)
	print(df)
