# encoding=utf-8
import json
from pandas import DataFrame
from collections import Counter
import numpy as np

def group_up():
	data = json.loads(open('./bookmarks.converted.json').read())
	frame = DataFrame(data)
	result = frame.groupby('created').agg('count').to_json()
	print result

if __name__ == "__main__":
	group_up()