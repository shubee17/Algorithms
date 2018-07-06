import sys

def merge_sort(array):
	if len(array) > 1:
		mid = len(array)//2
		leftmost = array[:mid]
		rightmost = array[mid:]
		merge_sort(leftmost)
		merge_sort(rightmost)
		i=j=k = 0
		while i<len(leftmost) and j<len(rightmost):
			if leftmost[i] < rightmost[j]:
				array[k] = leftmost[i]
				i += 1
			else:
				array[k] = rightmost[j]
				j += 1
			k += 1
		while i<len(leftmost):
			array[k] = leftmost[i]
			i += 1
			k += 1
		while j<len(rightmost):
			array[k] = rightmost[j]
			j += 1
			k += 1
	return(array)

array = sys.argv[1]
array = map(int, array.split(","))
print merge_sort(array)
