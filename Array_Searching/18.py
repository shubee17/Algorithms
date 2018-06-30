# Find the peak element

import sys

def peak_ele(Array):
	print "Peak Element of given Array =>",
	for i in range(len(Array)):
		if i == 0:
			if Array[i] > Array[i+1]:
				print Array[i]
				break
			else:
				pass
		else:
			if i == len(Array)-1:
				if Array[i] > Array[i-1]:
					print Array[i]
					break
				else:
					pass
			else:
				if Array[i] > Array[i-1] and Array[i] > Array[i+1]:
					print Array[i]
					break
				else:
					pass



Array = sys.argv[1]
Array = map(int, Array.split(","))
peak_ele(Array)
