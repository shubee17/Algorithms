# Find the missing number

import sys

def missing_no(Array):
	print "Missing number =>",
	for i in range(len(Array)):
		if i == len(Array) - 1:
			break
		if Array[i]+1 == Array[i+1]:
			pass
		else:
			print Array[i]+1,

Array = sys.argv[1]
Array = map(int, Array.split(","))
Array.sort()
missing_no(Array)
