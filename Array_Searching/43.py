# Search an element in an array where difference between adjacent elements is 1

import sys

def srch_ele(Array,x):
	flag = 0
	for i in range(len(Array)):
		if Array[i] == int(x):
			flag = 1
			print "Element",Array[i],"found at index",i
			break
		else:
			pass
	if flag == 0:
		print "Element Not Found At Any Index"
	else:
		pass

Array = sys.argv[1]
x = sys.argv[2]
Array = map(int, Array.split(","))
srch_ele(Array,x)
