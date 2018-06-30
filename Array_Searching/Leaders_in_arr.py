# Leaders in an array

import sys

def Leaders(Array):
	print "All Leaders in an Array =>",
	for i in range(len(Array)):
		if i != len(Array) - 1:
			if Array[i] > max(Array[i+1:]):
				print Array[i],
			else:
				pass
		else:
			print Array[i]

# 16,17,4,3,5,2
Array = sys.argv[1]
Array = map(int, Array.split(","))
Leaders(Array)
