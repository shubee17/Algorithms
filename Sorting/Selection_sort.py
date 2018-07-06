import sys

def selection_sort(array):
	for i in range(len(array)):
		for j in range(i+1,len(array)):
			if array[i] > array[j]:
				temp = array[i]
				array[i] = array[j]
				array[j] = temp
	return(array)
	
array = sys.argv[1]
array = map(int, array.split(","))
print selection_sort(array)






