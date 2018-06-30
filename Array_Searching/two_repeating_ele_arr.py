# Find the two repeating elements in a given array

import sys

def two_rep_ele(Array):
	table = {}
	for element in Array:
		if element in table:
			table[element] += 1
		elif element not in table:
			table[element] = 1
		else:
			table[element] = 0
	
	flag = 0
	print "Two Repeating Elements in a given Array =>",
	for element in table:
		if table[element] == 2:
			print element,
			flag = 1
		else:
			pass
	if flag == 0:
		print "None"
	else:
		pass


Array = sys.argv[1]
Array = map(int, Array.split(","))
two_rep_ele(Array)
