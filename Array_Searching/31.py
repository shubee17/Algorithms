# Find the number occurring odd no of times

import sys

def occ_odd(Array):
	table = {}
	for element in Array:
		if element in table:
			table[element] += 1
		elif element not in table:
			table[element] = 1
		else:
			table[element] = 0
	print "Number of elements occurring odd no. of times =>",
	for ele in table:
		if int(table[ele])%2 == 0:
			pass	
		else:
			print ele,

Array = sys.argv[1]
Array = map(int, Array.split(","))
occ_odd(Array) 
