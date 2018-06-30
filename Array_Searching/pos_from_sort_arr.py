# Find position of an element in a sorted array of infinite numbers

import sys

def pos_ele(Array,ele):
	flag = 0
	for index in range(len(Array)):
		if Array[index] == int(ele):
			print "Element Found at Position =>",index+1
			flag = 1
			break
		else:
			flag = 0
	if flag == 0:
		print "Element Not Found at any Position"
	else:
		pass
Array = sys.argv[1]
ele = sys.argv[2]
Array = map(int, Array)
pos_ele(Array,ele)
