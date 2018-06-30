#Equilibrium index of an array

import sys

def equi_ind(Array):
	sum1,sum2 = 0,0
	j = len(Array) - 1
	preffix,suffix = [],[]
	for i in range(len(Array)):
		sum1 = sum1 + Array[i]
		preffix.append(sum1)
		sum2 = sum2 + Array[j]
		suffix.append(sum2)
		j -= 1
	
	suffix_rev = suffix[::-1]
	for i in range(len(suffix_rev)):
		if suffix_rev[i] == preffix[i]:
			print "Equilibrium Index of an Array => ",i
			break
		else:
			pass


#-1,2,3,0,3,2,-1
#-2,5,3,1,2,6,-4,2
Array = sys.argv[1]
Array = map(int, Array.split(","))
equi_ind(Array) 
