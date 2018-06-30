# Find all triplet with zero sum

import sys

def zero_sum_trip(Array,n,combos,cnt):
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
			combos = zero_sum_trip(r_list,n,combos,cnt)
		return combos

Array = sys.argv[1]
r = sys.argv[2]
Array = map(int, Array.split(","))
n,cnt = 3,0
combos = []
zero_sum_trip(Array,n,combos,cnt)

sumi = 0
for i in range(len(combos)):
	if sum(combos[i]) == int(r):
		sumi += 1
	else:
		pass
print "There are ",sumi, "Triplet with Zero Sum"

