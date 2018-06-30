# Smallest Difference Triplet from three array

import sys

def maximum(a,b,c):
	return max(max(a,b),c)

def minimum(a,b,c):
	return min(min(a,b),c)

def small_trip(Array,Array1,Array2):
	Array.sort()
	Array1.sort()
	Array2.sort()
	r_max = r_mid = r_min = 0
	i = j = k = 0
	diff = 2147483647
	while (i < len(Array) and j < len(Array1) and k < len(Array2)):
		sumi = Array[i] + Array1[j] + Array2[k] 
		maxi = maximum(Array[i],Array1[j],Array2[k])
		mini = minimum(Array[i],Array1[j],Array2[k])
		if (mini == Array[i]):
			i += 1
		elif (mini == Array1[j]):
			j += 1
		else:
			k += 1
		if (diff > (maxi - mini)):
			diff = maxi - mini
			r_max = maxi
			r_mid = sumi - (maxi + mini)
			r_min = mini
		else:
			pass
	print r_max,r_mid,r_min 

Array = sys.argv[1]
Array1 = sys.argv[2]
Array2 = sys.argv[3]
Array = map(int, Array.split(","))
Array1 = map(int, Array1.split(","))
Array2 = map(int, Array2.split(","))
small_trip(Array,Array1,Array2)
