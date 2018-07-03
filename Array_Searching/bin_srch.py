# Binary search in sorted vector of pairs

import sys

def bin_srch(Array):
	k = str(raw_input("Enetr the key =>"))
	mid = len(Array) // 2
	left = Array[:mid]
	right = Array[mid:]
	flag = 0
	if left[-1][0] > k or left[-1][0] == k:
		for i in range(len(left)):
			if left[i][0] == k:
				print "Found"
				flag = 1
			else:
				pass
		if flag == 0:
			print "Not Found"
		else:
			pass
	else:
		for i in range(len(right)):
			if right[i][0] == k:
				print "Found"
				flag = 1
			else:
				pass
		if flag == 0:
			print "Not Found"
		else:
			pass
		

n = int(raw_input())
Array = []
for i in range(int(n)):
	a = str(raw_input())
	a = a.split(" ")
	Array.append(a)
bin_srch(Array)
