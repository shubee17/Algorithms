# Search an element in an unsorted array using minimum number of comparisons

import sys

def srch_ele(Array,k):
	flag = 0
	n = len(Array)
	for i in range(len(Array)):
		if i == (len(Array) - i+1):
			break
		if int(k) == Array[i] or int(k) == Array[n-(i+1)]:
			print "Found"
			flag = 1
			break
		else:
			pass
	if flag == 0:
		print "Not Found"
	else:
		pass

Array = sys.argv[1]
k = sys.argv[2]
Array = map(int, Array.split(","))
srch_ele(Array,k)
