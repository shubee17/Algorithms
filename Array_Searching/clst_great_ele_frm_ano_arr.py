# Closet greater element for every array element from another array

import sys

def clst_grt_ele(Array,Array1):
	n,Array2 = 0,[]
	mini = 1000000
	while (n < len(Array1)):
		for i in range(len(Array)):
			if Array1[n] < Array[i]:
				if Array[i] < mini:
					mini = Array[i]
		if mini == 1000000:
			Array2.append(-1)
		else:
			Array2.append(mini)
		mini = 1000000
		n += 1
	print "Closet Greater Element Array =>",Array2 
			
				 

Array = sys.argv[1]
Array1 = sys.argv[2]
Array = map(int, Array.split(","))
Array1 = map(int, Array1.split(","))
Array.sort()
clst_grt_ele(Array,Array1) 
