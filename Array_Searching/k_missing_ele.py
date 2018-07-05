# kth missing element in sorted array

import sys

def k_missing(Array,k):
	difference = 0
	count = 0
	for i in range(len(Array)):
		if i == len(Array) - 1:
			print "No Missing Element"
			break
		if (Array[i+1] - Array[i]) == 1:
			pass
		else:		
			difference = (Array[i+1] - Array[i]) - 1
			count += difference
			if count == int(k):
				print Array[i+1] - 1
				break
			elif count > int(k):
				x = count - int(k)
				print Array[i+1] - x
				break
			else:
				pass

Array = sys.argv[1]
k = sys.argv[2]
Array = map(int, Array.split(","))
k_missing(Array,k)
