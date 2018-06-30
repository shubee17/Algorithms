# Find the two numbers with odd occurrences in an unsorted array

import sys

def occ_two(Array):
	table = {}
	for element in Array:
		if element in table:
			table[element] += 1
		elif element not in table:
			table[element] = 1
		else:
			table[element] = 0

	print "Odd Occurrences =>",
	for ele in table:
		if int(table[ele])%2 == 0:
			pass
		else:
			print ele,

Array = sys.argv[1]
Array = map(int, Array.split(","))
occ_two(Array)
