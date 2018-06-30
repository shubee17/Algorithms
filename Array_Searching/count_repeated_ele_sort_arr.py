# Count of only repeated element in a sorted array of consecutive elements

import sys

def rep_count(Array):
	cnt = 0
	for i in range(len(Array)):
		if i == len(Array) - 1:
			cnt += 1
			break 
		if Array[i] == Array[i+1]:
			ele = Array[i]
			cnt += 1
		else:
			pass
	print ele," => ",cnt

Array = sys.argv[1]
Array = map(int, Array.split(","))
rep_count(Array)
