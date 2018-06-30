# Print all triplet in sorted array

import sys

def sort_trip(Array,n,combos):
	if combos is None:
		combos = []
	if len(Array) == n:
		if combos.count(Array) == 0:
			combos.append(Array)
			combos.sort()
		return combos
	else:
		for i in range(len(Array)):
			r_list = Array[:i] + Array[i+1:]
			combos = sort_trip(r_list,n,combos)
		return combos
Array = sys.argv[1]
Array = map(int, Array.split(","))
n,combos = 3,[]
sort_trip(Array,n,combos)

print "All Triplet in a sorted manner =>",combos
