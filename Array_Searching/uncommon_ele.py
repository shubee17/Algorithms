#Print Uncommon elements from two sorted arrays

import sys

def uncomm_ele(Array1,Array2):
	i = j = k = 0
	while (i < len(Array1) and j < len(Array2)):
		if Array1[i] < Array2[j]:
			print Array1[i],
			i += 1
		elif Array1[i] > Array2[j]:
			print Array2[j],
			j += 1
		else:
			i += 1
			j += 1

	while (i < len(Array1)):
		print Array1[i],
		i += 1
	while (j < len(Array2)):
		print Array2[j],
		j += 1	

Array1 = sys.argv[1]
Array2 = sys.argv[2]
Array1 = map(int, Array1.split(","))
Array2 = map(int, Array2.split(","))
uncomm_ele(Array1,Array2)
