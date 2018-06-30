# Find the repeating and missing element

import sys

def rep_miss(Array):
	Array.sort()
	for i in range(len(Array)):
		if i == len(Array) - 1:
			break
		if Array[i]+1 == Array[i+1]:
			pass
		else:
			if Array[i] == Array[i+1]:
				print "Repeated Element =>",Array[i]
			else:
				print "Missing Element =>",Array[i]+1

Array = sys.argv[1]
Array = map(int, Array.split(","))
rep_miss(Array)
