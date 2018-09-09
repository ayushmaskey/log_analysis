
from pull_pickle import get_from_pickle


fileName = './pickle/test.pickle'

df = get_from_pickle()

if __name__ == "__main__":
	# push_to_pickle()
	df = get_from_pickle()
	print(df.keys())