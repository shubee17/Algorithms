# Find the first repeating element in an array of integer

import sys

def frst_rep(Array):
	for i in range(len(Array)):
		if Array[i] in Array[i+1:]:
			print "First Repeating Element =>",Array[i]
			flag = 1
			break
		else:
			pass
	if flag == 0:	
		print "No Repeating Element"
	else:
		pass

Array = sys.argv[1]
Array = map(int, Array.split(","))
frst_rep(Array)
