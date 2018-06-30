# Find a Number such that sum of two equals to third element

import sys

def sum_of_two(Array,n,combos):
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
			combos = sum_of_two(r_list,n,combos)
		return combos

Array = sys.argv[1]
Array = map(int, Array.split(","))
n,combos = 3,[]
sum_of_two(Array,n,combos)

print "Sum of two Equals to Third =>",
for i in range(len(combos)):
	if int(combos[i][0] + combos[i][1]) == int(combos[i][2]):
		print combos[i],
	else:
		pass
