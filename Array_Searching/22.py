# Maximum triplet sum in array

import sys

def max_tri(Array):
	maxA = -1000000
	maxB = -1000000
	maxC = -1000000
	for i in range(len(Array)):
		if Array[i] > maxA:
			maxC = maxB
			maxB = maxA
			maxA = Array[i]
		elif Array[i] > maxB:
			maxC = maxB
			maxB = Array[i]
		elif Array[i] > maxC:
			maxC = Array[i]
	
	return (maxA + maxB + maxC)

Array = sys.argv[1]
Array = map(int, Array.split(","))
print "Maximum triplet sum in array =>",max_tri(Array)
