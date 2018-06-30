#Two Pointers Technique

import sys

def two_pointers(Array,x):
	i = 0
	j = len(Array) - 1
	list1 = []
	while(i < j):
		print Array[i:j]
		if ((Array[i] + Array[j]) == int(x)):
			return True
		elif (Array[i] + Array[j]) < int(x):
			i += 1
		else:
			j -= 1
	return False

Array = sys.argv[1]
x = sys.argv[2]
Array = map(int, Array.split(","))
print two_pointers(Array,x)
