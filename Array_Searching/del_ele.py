# Delete an element from array(Using two traversal and one traversal)

import sys

def del_ele(Array,k):
	n = len(Array) - 1
	for i in range(len(Array)):
		if Array[i] == int(k):
			del(Array[i])
			break
		elif Array[n] == int(k):
			del(Array[n])
			break
		else:
			n -= 1
			pass
	print Array

Array = sys.argv[1]
k = sys.argv[2]
Array = map(int, Array.split(","))
del_ele(Array,k)
