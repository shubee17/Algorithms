# Count frequencies of all elements in array in O(1) extra space and O(n) time

import sys

def cnt_freq(Array):
	table = {}
	for element in Array:
		if element in table:
			table[element] += 1
		elif element not in table:
			table[element] = 1
		else:
			table[element] = 0
	for ele in table:
		print ele, "=>" ,table[ele]

Array = sys.argv[1]
Array = map(int, Array.split(","))
cnt_freq(Array)
