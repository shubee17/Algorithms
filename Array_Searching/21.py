# Find subarray with given sum

import sys

def sub_arr_sum(Array,x):
	flag = 0
	for i in range(len(Array)):
		for j in range(i+1,len(Array)+1):
			if sum(Array[i:j]) == int(x):
				print i,j-1
				flag = 1
			else:		
				pass
	if flag == 0:
		print "No Subarray Found"
	else:
		pass

Array = sys.argv[1]
x = sys.argv[2]
Array = map(int, Array.split(","))
sub_arr_sum(Array,x)
