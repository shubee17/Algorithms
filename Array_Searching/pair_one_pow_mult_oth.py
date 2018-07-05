#Pairs such that one is a power multiple of other

import sys
import math

def pair_pow(Array,k,n):
	sol = 0
	Array.sort()
	print "Pairs => ",
	for i in range(0,n):
		for j in range(i+1,n):
			x = 0
			while((Array[i] * math.pow(int(k), x)) <= Array[j]):
				if ((Array[i] * math.pow(int(k), x)) == Array[j]):
					print "(",Array[i],",",Array[j],")",
					sol += 1
					break
				x += 1
	print "\nTotal Count => ",sol

Array = sys.argv[1]
k = sys.argv[2]
Array = map(int, Array.split(","))
n = len(Array)
pair_pow(Array,k,n)
