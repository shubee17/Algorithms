# Count 1's in a sorted array

import sys

def cnt_ones(Array):
	cnt = 0
	for i in Array:	
		if i == 1:
			cnt += 1
		else:
			pass
	print "No of 1's in a Array =>",cnt

Array = sys.argv[1]
Array = map(int, Array.split(","))
cnt_ones(Array)
