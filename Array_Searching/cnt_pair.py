# Count pairs with given sum

import sys

def cnt_pair(Array,k):
	cnt = 0
	for i in range(len(Array)):
		for j in range(i+1,len(Array)):
			if (Array[i] + Array[j]) == int(k):
				cnt += 1
				print Array[i],Array[j]
	print "Count => ",cnt

Array = sys.argv[1]
k = sys.argv[2]
Array = map(int, Array.split(","))
cnt_pair(Array,k)
