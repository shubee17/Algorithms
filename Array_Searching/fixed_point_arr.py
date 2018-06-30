# Find a Fixed point in a given array

import sys

def fixed_point(Array):
	flag = 0
	print "Fixed point in a given array =>",
	for i in range(len(Array)):
		if Array[i] == i:
			print i,
			flag = 1
		else:
			pass
	if flag == 0:
		print "None"
	else:
		pass

Array = sys.argv[1]
Array = map(int, Array.split(","))
fixed_point(Array)
