# Find the four element that sum to a given value

import sys

def sum_value(Array,x,combos,n):
	if combos is None:
		combos = []
	if len(Array) == n:
		if combos.count(Array) == 0:
			combos.append(Array)
		return combos
	else:
		for i in range(len(Array)):
			r_list = Array[:i] + Array[i+1:]
			combos = sum_value(r_list,x,combos,n)
		return combos


Array = sys.argv[1]
x = sys.argv[2]
combos,n = [],4
Array = map(int, Array.split(","))
sum_value(Array,x,combos,n)

print "Four Element that sum to given value =>",
flag = 0
for i in range(len(combos)):
	if sum(combos[i]) == int(x):
		flag = 1
		print combos[i],
	else:
		pass

if flag == 0:
	print "No such four Element"
else:
	pass
