# Find the first, second and third minimum elements in an array 

import sys

def min_ele(Array):
	m_frst = m_sec = m_thrd = 1000000
	for i in range(len(Array)):
		if Array[i] < m_frst:
			m_thrd = m_sec
			m_sec = m_frst
			m_frst = Array[i]
		elif Array[i] < m_sec:
			m_thrd = m_sec
			m_sec = Array[i]
		elif Array[i] < m_thrd:
			m_thrd = Array[i]
	print "First Minimum => ",m_frst
	print "Second Minimum => ",m_sec
	print "Third Minimum => ",m_thrd


Array = sys.argv[1]
Array = map(int, Array.split(","))
min_ele(Array)
