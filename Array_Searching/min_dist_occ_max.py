# Minimum Distance between two occurrences of maximum

import sys

def min_dist_max_occ(Array):
	max_ele = Array[0]
	min_dis = len(Array)
	index = 0
	for i in range(1,len(Array)):
		if max_ele == Array[i]:
			min_dis = min(min_dis, (i - index))
			index = i
		elif max_ele < Array[i]:
			max_ele = Array[i]
			min_dis = len(Array)
			index = i
		else:
			pass
	print min_dis


Array = sys.argv[1]
Array = map(int, Array.split(","))
min_dist_max_occ(Array)
