__author__ = 'keechow'

"""
name: det-module.py
objectives: determine various characteristics of a given number
     *det_num_sum()
     *det_odd_even()
     *det_num_cat()
     *det_d0()
     *det_d0d1()
     *det_d0d1d2()
     *det_d1d2d3()
     *det_d2d3()
"""

def det_num_sum(num):
	if (len(num) == 1):
		return int(num)
	else:
		total = int(num[0]) + det_num_sum(num[1:])
		return total

