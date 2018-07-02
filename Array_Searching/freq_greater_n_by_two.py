# Find element in a sorted array whose frequency is greater then or equal to n/2

import sys

def ele_freq(Array,n):
	cnt = 0
	for i in range(len(Array)):
		if i == len(Array) - 1:
			cnt += 1
			if (cnt == n or cnt > n):
				print Array[i]
				break
			else:
				break 
		if Array[i] == Array[i+1]:
			cnt += 1
		else:
			cnt += 1
			if (cnt == n or cnt > n):
				print Array[i]
				cnt = 0
			else:
				cnt = 0

Array = sys.argv[1]
Array = map(int, Array.split(","))
n = len(Array)/2
ele_freq(Array,n)
