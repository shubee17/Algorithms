#Find the only repetitive element between 1 to n-1

import sys

def rep_ele(Array):
	table = {}
	for element in Array:
		if element in table:
			table[element] += 1
		elif element not in table:
			table[element] = 1
		else:
			table[element] = 0

	print "Repetitive Element in Array => ",
	for ele in table:
		if table[ele] > 1:
			print ele,
		else:
			pass 




Array = sys.argv[1]
Array = map(int, Array)
rep_ele(Array)

