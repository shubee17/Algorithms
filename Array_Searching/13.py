#Ceiling of a sorted array

import sys

def f_ceil(Arr,x):
	mini = []
	for i in range(len(Arr)):
		if Arr[i] > int(x) or Arr[i] == int(x):
			mini.append(Arr[i])
		else:
			pass
	print "Ceiling of an sorted array =>",min(mini)

def ceil(Array,x):
	mid = len(Array)//2
	left = Array[:mid]
	right = Array[mid:]
	if left[-1] == int(x) or left[-1] > int(x):
		f_ceil(left,x)
	else:
		f_ceil(right,x)


Array = sys.argv[1]
x = sys.argv[2]
Array = map(int, Array.split(","))
ceil(Array,x)
