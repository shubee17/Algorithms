import sys

def Bubble_sort(array):
	for i in range(len(array)):
		for j in range(len(array)-1,i,-1):
			if array[j] < array[j-1]:
				temp = array[j]
				array[j] = array[j-1]
				array[j-1] = temp
	return(array)

array = sys.argv[1]
array = map(int, array.split(","))
print Bubble_sort(array)
