# Find if there is a sub-array with zero sum

import sys

def sub_array(Array):
	flag = 0
	print "Sub_Array with sum zero =>",
	for i in range(len(Array)):
		for j in range(i+1,len(Array)+1):
			if len(Array[i:j]) > 1:
				if sum(Array[i:j]) == int(x):
					flag = 1
					print Array[i:j],
				else:
					pass
			else:
				pass
	if flag == 0:
		print "None"
	else:
		pass
				


Array = sys.argv[1]
x = sys.argv[2]
Array = map(int, Array.split(","))
sub_array(Array)
