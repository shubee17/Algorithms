# Number of unique triplets whose XOR is zero

import sys

def uni_trip_xor(Array,n,combos):
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
			combos = uni_trip_xor(r_list,n,combos)
		return combos

Array = sys.argv[1]
Array = map(int, Array.split(","))
n,combos = 3,[]
r = sys.argv[2]
uni_trip_xor(Array,n,combos)

print "No of Unique Triplets whose XOR is zero =>",
for i in range(len(combos)):
	if sum(combos[i]) == int(r):
		print combos[i],
	else:
		pass
