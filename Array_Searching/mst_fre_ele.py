#Most frequent element in an array

import sys

def mst_freq_ele(Array):
	table = {}
	for element in Array:
		if element in table:
			table[element] += 1
		elif element not in table:
			table[element] = 1
		else:
			table[element] = 0

	maxi = -1

	for ele in table:
		if table[ele] > maxi:
			element = ele
			maxi = table[element]
		else:
			pass
	print element,"appears",maxi,"times in array which is maximum frequency."

Array = sys.argv[1]
Array = map(int, Array.split(","))
mst_freq_ele(Array)
