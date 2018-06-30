#Majority Element

import sys

def maj_ele(Array):
	table = {}
	x = len(Array)/2
	list1,flag = [],0
	print "Majority Element =>",
	for element in Array:
		if element in table:
			table[element] += 1
			if table[element] > x:
				if table not in list1:
					list1.append(element)
					flag = 1
					print element,
				else:
					pass
			else:
				pass
		elif element not in table:
			table[element] = 1
		else:
			table[element] = 0
	if flag == 0:
		print "None"
	else:
		pass


Array = sys.argv[1]
Array = map(int, Array.split(","))
maj_ele(Array)
