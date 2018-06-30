# Count number of occurrences(or frequency) in a sorted array

import sys

def occ_sorted(Array):
	cnt = 0
	for i in range(len(Array)):
		if i == len(Array) - 1:
			cnt += 1
			print Array[i]," =>",cnt
			break
		if Array[i] == Array[i+1]:
			cnt += 1
		else:
			cnt += 1
			print Array[i]," =>",cnt
			cnt = 0



Array = sys.argv[1]
Array = map(int, Array.split(","))
occ_sorted(Array)
