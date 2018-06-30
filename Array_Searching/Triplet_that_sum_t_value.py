# Find a triplet that sum to a given value

import sys

def combinations(Array,n,combos):
	if combos is None:
		combos = []
	if len(Array) == n:
		if combos.count(Array) == 0:
			combos.append(Array)
			combos.sort()
		return combos
	else:
		for i in range(len(Array)):
			refined_list = Array[:i] + Array[i+1:]
			combos = combinations(refined_list,n, combos)
		return combos

Array = sys.argv[1]
r = sys.argv[2]
Array = map(int, Array.split(","))
n = 3
combos = []
combinations(Array,n,combos)

flag = 0
for i in range(len(combos)):
	if sum(combos[i]) == int(r):
		print "Yes Present =>",combos[i]
		flag = 1
	else:
		pass
if flag == 0:
	print "Not Present"
else:
	pass
