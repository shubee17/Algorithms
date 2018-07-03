# Count inversion of size three in a given array

import sys

def inv_size(n,combos,Array):
	if combos is None:
		combos = []
	if len(Array) == n:
		if combos.count(Array) == 0:
			if Array[0] > Array[1] > Array[2]:
				combos.append(Array)
		return combos
	else:
		for i in range(len(Array)):
			r_list = Array[:i] + Array[i+1:]
			combos = inv_size(n,combos,r_list)
		return combos

Array = sys.argv[1]
Array = map(int, Array.split(","))
n = 3
combos = []
inv_size(n,combos,Array)

print combos
