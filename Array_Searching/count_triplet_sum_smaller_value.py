# Count Triplet that sum smaller than a given value

import sys

def cnt_trip_sum(Array,n,combos):
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
			combos = cnt_trip_sum(r_list,n,combos)
		return combos
Array = sys.argv[1]
Array = map(int, Array.split(","))
n,combos = 3,[]
r = sys.argv[2]
cnt_trip_sum(Array,n,combos)

print "All Triplet that sum smaller than a given value =>",
for i in range(len(combos)):
	if sum(combos[i]) < int(r):
		print combos[i],
	else:
		pass
