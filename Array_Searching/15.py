# Check Majority element in a sorted array

import sys

def maj_ele(Array):
	list1,flag = [],0
	x = len(Array)/2
	print "Majority Element in an Sorted Array =>",
	for i in range(len(Array)):
		if list1 == [] or list1[0] == Array[i]:
			list1.append(Array[i])
		else:
			length = len(list1)
			if len(list1) > x:
				print list1[0],
				flag = 1
				list1 = []
				list1.append(Array[i])
			else:
				list1 = []
				list1.append(Array[i])
	if flag == 0:
		print "None"
	else:
		pass


Array = sys.argv[1]
Array = map(int, Array.split(","))
maj_ele(Array)
