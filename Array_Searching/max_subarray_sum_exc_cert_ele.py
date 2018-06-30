# Maximum subarray sum excluding certain element

import sys

def max_subarr(Array):
	maxi = 0
	for i in range(len(Array)):
		for j in range(i+1,len(Array)+1):
			if len(Array[i:j]) > 1: 
				if sum(Array[i:j]) > maxi:
					maxi = sum(Array[i:j])
					subarr = Array[i:j]
				else:
					pass
			else:
				pass
	print "Maximum Subarray ",subarr," with maximum sum",maxi

Array = sys.argv[1]
Array = map(int, Array.split(","))
max_subarr(Array)
