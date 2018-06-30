# Searching in an array where adjacent differ by at most k

import sys

def search_key(Array,key):
	flag = 0
	for i in range(len(Array)):
		if Array[i] == int(key):
			print "The key Found at index => ",i
			break
		else:
			pass
	if flag == 1:
		print "Key Does'nt Exists!!!"
	else:
		pass


Array = sys.argv[1]
key = sys.argv[2]
Array = map(int, Array)
search_key(Array,key)
