# Replacing an element makes array elements consecutive

import sys

def rep_ele(Array):
	if len(Array) > 1:
		mid = len(Array) // 2
		left = Array[:mid]
		right = Array[mid:]
		rep_ele(left)
		rep_ele(right)
		i = j = k = 0
		while (i < len(left) and j < len(right)):
			if left[i] < right[j]:
				Array[k] = left[i]
				i += 1
			else:
				Array[k] = right[j]
				j += 1
			k += 1
		while i < len(left):
			Array[k] = left[i]
			i += 1
			k += 1
		while j < len(right):
			Array[k] = right[j]
			j += 1
			k += 1
	return Array



Array = sys.argv[1]
Array = map(int, Array.split(","))
rep_ele(Array)

print Array
for i in range(len(Array)):
	if i == len(Array) - 1:
		print "Array is already in consecutive manner"
		break
	if Array[i] == Array[i+1] - 1:
		pass
	else:
		if Array[i] != Array[i+1] - 1:	
			if Array[i] != Array[i+1] - 2:
				print "No,we cannot replace element"
				break
			else:
				print "Yes,we can replace element"
				break
