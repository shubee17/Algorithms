# Given an array Array[] and a number x,check for pair in Array[] with sum as x

import sys

def pair_sum(Array,x):
	for i in range(len(Array)-1):
		for j in range(i+1,len(Array)):
			if (Array[i] + Array[j]) == int(x):
				print Array[i],Array[j]
			else:
				pass


Array = sys.argv[1]
x = sys.argv[2]
Array = map(int, Array)
pair_sum(Array,x)
