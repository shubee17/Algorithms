# Median of two sorted arrays with different sizes in O(log(min(n,m)))

import sys

def mid_ele(Array1,Array2,Array3):
	i = j = k = 0
	while (i < len(Array1) and j < len(Array2)):
		if Array1[i] < Array2[j]:
			Array3[k] = Array1[i]
			i += 1
		else:
			Array3[k] = Array2[j]
			j += 1
		k += 1
	while (i < len(Array1)):
		Array3[k] = Array1[i]
		i += 1
		k += 1
	while (j < len(Array2)):
		Array3[k] = Array2[j]
		j += 1
		k += 1
	if len(Array3)%2 == 0:
		mid = len(Array3) // 2
		x = Array3[mid] + Array3[mid-1]
		print "The Median is =>",x/2
	else:
		mid = len(Array3) // 2
		print "The Median is => ",Array3[mid]
	

Array1 = sys.argv[1]
Array2 = sys.argv[2]
Array1 = map(int, Array1.split(","))
Array2 = map(int, Array2.split(","))
Array3 = [0] * (len(Array1) + len(Array2))
mid_ele(Array1,Array2,Array3)
