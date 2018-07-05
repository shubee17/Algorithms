# Maximum difference between two subsets of m elements

import sys

def max_diff_subs(Array,k):
	Array.sort() # Use Merge Sort
	j = len(Array) - 1
	maxi = mini = 0
	for i in range(int(k)):
		mini += Array[i]
		maxi += Array[j]
		j -= 1
	print maxi - mini


Array = sys.argv[1]
k = sys.argv[2]
Array = map(int, Array.split(","))
max_diff_subs(Array,k)
