# Given a sorted array and a number x ,find the pair in array whose sum is closet to x

import sys

def pair_cls_x(Array,x):
	list1,a,b = [],[],[]
	for i in range(len(Array)):
		for j in range(i+1,len(Array)):
			s = []
			s.append(Array[i])
			s.append(Array[j])
			if list1.count(s) == 0:
				list1.append(s)
			else:
				pass
	print list1
	cnt = abs(sum(list1[0]) - int(x))
	for i in range(1,len(list1)):
		if abs(sum(list1[i]) - int(x)) < cnt:
			cnt = abs(sum(list1[i]) - int(x))
			ele = list1[i]
		else:
			pass
	print ele,
	print cnt
	


Array = sys.argv[1]
Array = map(int, Array.split(","))
x = sys.argv[2]
pair_cls_x(Array,x)

