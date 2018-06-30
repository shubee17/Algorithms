# Search,Insert and delete in an unsorted array

import sys

def srh_ins_del(Array,Ele):
	# Search
	flag = 0
	for element in range(len(Array)):
		if Array[element] == int(Ele):
			flag = 1
			print "Element Successfully Found at position =>",element + 1
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
	for element in range(len(Array)):
		if (element + 1) == int(position):
			flag = 1
			Array[element] = int(Element)
			print "Element Successfully Inserted =>",Array
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
	for element in range(len(Array)):
		if (element + 1) == int(position):
			flag = 1
			del(Array[element])
			print "Element Successfully Deleted =>",Array
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
