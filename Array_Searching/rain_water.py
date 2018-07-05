# Trapping rain water

import sys

def trap_water(Array, n):
	left = [0]*n
	right = [0]*n
	water = 0
	left[0] = Array[0]
	for i in range(1,n):
		left[i] = max(left[i-1], Array[i])
	
	right[n-1] = Array[n-1]
	for i in range(n-2, -1, -1):
		right[i] = max(right[i+1], Array[i])

	for i in range(0, n):
		water += min(left[i],right[i]) - Array[i]
	return water


Array = sys.argv[1]
Array = map(int, Array.split(","))
n = len(Array)
print trap_water(Array, n)
