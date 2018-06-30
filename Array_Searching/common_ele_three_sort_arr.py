# Find common elements in three sorted array

import sys

def comm_ele(Array,Array1,Array2):
	Array3 = []
	flag = 0
	for element in Array:
		if element in Array1:	
			Array3.append(element)
		else:
			pass

	print "Common In Three Sorted Array => ",
	for element in Array3:
		if element in Array2:
			flag = 1
			print element,
		else:
			pass
	if flag == 1:
		pass
	else:
		print "None"



Array = sys.argv[1]
Array1 = sys.argv[2]
Array2 = sys.argv[3]
Array = map(int, Array)
Array1 = map(int, Array1)
Array2 = map(int, Array2)
comm_ele(Array,Array1,Array2)
