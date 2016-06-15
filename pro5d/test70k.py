"""
Name: test70k.py
Objective: Check 5D numbers (70000 - 79999) against result from 2016 apr 03 to 2016 jun 01

"""

from num_generator_5d import generate_5d_numrange
from file_handler import read5d_result_w_draw_no

num5d_70k = generate_5d_numrange(70000)

result_5d_70k = open("5D_result_repeat7.txt", "r")

result_5d_70k_num_only = []
num5d_70k_after_filtered = []    #store 5D num that was not drawn

counter = 0
for each in result_5d_70k:
	result_5d_70k_num_only.append(each[2:7])
	counter += 1

for each in num5d_70k:
	if not each in result_5d_70k_num_only:
		num5d_70k_after_filtered.append(each)

result_5d_latest = read5d_result_w_draw_no("5D_result.txt")

result_matched = []
for each_num in num5d_70k_after_filtered:
	for each_draw in result_5d_latest:
		if each_num in each_draw:
			result_matched.append(each_draw)

print result_matched







