#Find the pair with given difference


import sys

def pair_diff(Array,x):
	flag,list1 = 0,[]
	print "Pair with given difference => ",
	for i in range(len(Array)):
		for j in range(i+1,len(Array)):
			s = []
			s.append(Array[i])
			s.append(Array[j])
			if list1.count(s) == 0:
				list1.append(s)
				if abs(Array[i] - Array[j]) == int(x):
					flag = 1
					print s,
				else:
					pass
	if flag == 0:
		print "No such Pair"
	else:
		pass
	
			

Array = sys.argv[1]
x = sys.argv[2]
Array = map(int, Array.split(","))
pair_diff(Array,x)
