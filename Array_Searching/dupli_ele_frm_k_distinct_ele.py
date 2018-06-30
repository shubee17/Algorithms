# Check if a given array contains duplicate elements within k distinct from each other

import sys

def dup_ele(Array,k):
	for i in range(len(Array)):
		if i+int(k) > len(Array)-1:
			break
		if Array[i] == Array[i+int(k)]:
			print Array[i],"is repeated at distance",i+int(k) 
			return True
		else:
			pass
	return False


Array = sys.argv[1]
k = sys.argv[2]
Array = map(int, Array.split(","))
print dup_ele(Array,k)
