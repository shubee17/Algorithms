#least Frequent element in an array

import sys

def least_freq_ele(Array):
	table = {}
	for element in Array:
		if element in table:
			table[element] += 1
		elif element not in table:
			table[element] = 1
		else:
			table[element] = 0

	mini = 10000000000

	for ele in table:
		if table[ele] < mini:
			element = ele
			mini = table[ele]
		else:
			pass
	print element,"apppers",mini,"times in array which is minimum frequency."

Array = sys.argv[1]
Array = map(int, Array.split(","))
least_freq_ele(Array)
