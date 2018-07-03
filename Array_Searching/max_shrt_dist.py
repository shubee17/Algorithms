# Pair with given sum and maximum shortest distance from end

import sys

def max_short_dist(Array,k):
	mini = -10000000
	for i in range(len(Array)):
		for j in range(i+1,len(Array)):
			if (Array[i] + Array[j]) == int(k):
				if j > mini:
					mini = j
					ins = i
					ind = j
				else:
					pass
			else:
				pass

	print Array[ins],Array[ind]
	print max(ins+1,len(Array) - ind)

Array = sys.argv[1]
k = sys.argv[2]
Array = map(int, Array.split(","))
max_short_dist(Array,k)
