# Search,Insert and delete in an sorted array

import sys

def srh_ins_del(Array,Ele):
	# Search
	flag = 0
	mid = len(Array)//2
	left = Array[:mid]
	right = Array[mid:]
	if left[-1] == int(Ele) or left[-1] > int(Ele):
		for element in range(len(left)):
			if left[element] == int(Ele):
				flag = 1
				print "Element Successfully Found at position =>",element + 1
				break
			else:
				flag = 0
	else:
		for element in range(len(right)):
			if right[element] == int(Ele):
				flag = 1
				print "Element Successfully Found at position =>",len(left) + (element + 1)
				break
			else:
				flag = 0
	if flag == 0:
		print "Element Not Found!!! "
	else:
		pass
	
	#Insert
	print "\n"
	flag = 0
	position = int(raw_input("Enter the position which you want to be Insert element => "))
	Element = int(raw_input("Enter the element => "))
	mid = len(Array)//2
	left = Array[:mid]
	right = Array[mid:]
	if len(left) == int(position) or len(left) > int(position):
		for element in range(len(left)):
			if (element + 1) == int(position):
				flag = 1
				left[element] = int(Element)
				print "Element Successfully Inserted =>",left + right
				break
			else:
				flag = 0
	else:
		for element in range(len(right)):
			if (len(left) + (element + 1)) == int(position):
				flag = 1
				right[element] = int(Element)
				print "Element Successfully Inserted =>",left + right
				break
			else:
				flag = 0
		
	if flag == 0:
		print "Position Does'nt Exists!!!"
	else:
		pass

	#Delete
	print "\n"
	flag = 0
	position = int(raw_input("Enter the position which you want to be Delete element => "))
	mid = len(Array)//2
	left = Array[:mid]
	right = Array[mid:]
	if len(left) == int(position) or len(left) > int(position):
		for element in range(len(left)):
			if (element + 1) == int(position):
				flag = 1
				del(left[element])
				print "Element Successfully Deleted =>",left + right
				break
			else:
				flag = 0
	else:
		for element in range(len(right)):
			if (len(left) + (element + 1)) == int(position):
				flag = 1
				del(right[element])
				print "Element Successfully Deleted =>",left + right
				break
			else:
				flag = 0
	if flag == 0:
		print "Position Does'nt Exists!!!  "
	else:
		pass

Array = sys.argv[1]
Array = map(int, Array)
Ele = sys.argv[2]
srh_ins_del(Array,Ele)
