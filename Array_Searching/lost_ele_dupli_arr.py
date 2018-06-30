# Find lost element from a duplicated array

import sys

def lost_ele(Array,Array1):
	flag = 0
	for i in Array:
		if i not in Array1:
			print "Lost Element =>",i
			flag = 1
			break
		else:
			pass
	if flag == 0:
		print "No Lost Element"
	else:
		pass

Array = sys.argv[1]
Array1 = sys.argv[2]
Array = map(int, Array.split(","))
Array1 = map(int, Array1.split(","))
lost_ele(Array,Array1) 
