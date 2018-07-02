# Minimum absolute difference od adjacent elements in a circular array

import sys

def min_adj_diff(Array,n):
	if n < 2:
		return
	res = abs(Array[1] - Array[0])

	for i in range(2, n):
		res = min(res, abs(Array[i] - Array[i - 1]))
	res = min(res, Array[n - 1] - Array[0])
	print res


Array = sys.argv[1]
Array = map(int, Array.split(","))
n = len(Array)
min_adj_diff(Array,n)
