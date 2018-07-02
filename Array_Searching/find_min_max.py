# program to find minimum (or maximum) element of an array

import sys

def min_max(Array):
	mini = 1000000
	maxi = -1000000
	for i in range(len(Array)):
		if Array[i] < mini:
			mini = Array[i]
		elif Array[i] > maxi:
			maxi = Array[i]
	print "Maximum Element =>",maxi
	print "Minimum Element =>",mini

Array = sys.argv[1]
Array = map(int, Array.split(","))
min_max(Array)
