# Third largest element in an array of distinct array

import sys

def third_lar_ele(Array):
	mini = mid = maxi = 0
	for i in range(len(Array)):
		if Array[i] > maxi:
			mini = mid
			mid = maxi
			maxi = Array[i]
		elif Array[i] > mid:
			mini = mid
			mid = Array[i]
		elif Array[i] > mini:
			mini = Array[i]
	print "Largest Element in an Array =>",mini
Array = sys.argv[1]
Array = map(int, Array.split(","))
third_lar_ele(Array)
