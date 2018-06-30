# Check if there exists two elements in an array whose sum is equal to the sum of rest of the array

import sys

def Two_ele_rem_arr(Array,combos):
	index,list1,list2 = [],[],[]
	flag = 0
	for i in range(len(Array)):
		for j in range(i+1,len(Array)):
			ind = []
			ind.append(i)
			ind.append(j)
			index.append(ind)
	for i in range(len(index)):
		for j in range(len(Array)):
			if index[i][0] == j or index[i][1] == j:
				list1.append(Array[j])
			else:
				list2.append(Array[j])
		if sum(list1) == sum(list2):
			print list1," => ",list2
			flag = 1
			break
		else:
			list1,list2 = [],[]
	if flag == 0:
		print "Element do not exists"
	else:
		pass

Array = sys.argv[1]
combos = []
Array = map(int, Array.split(","))
Two_ele_rem_arr(Array,combos)
