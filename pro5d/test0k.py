"""
Name: test0k.py
Objective: Check 5D numbers (00000 - 09999) against result from 2016 apr 03 to 2016 jun 01

"""

from num_generator_5d import generate_5d_numrange
from file_handler import read5d_result_w_draw_no

num5d = generate_5d_numrange(90000)

result_5d = open("5D_result_repeat9.txt", "r")

result_5d_num_only = []
num5d_after_filtered = []    #store 5D num that was not drawn

counter = 0
for each in result_5d:
	result_5d_num_only.append(each[2:7])
	counter += 1

counter = 0
for each in num5d:    # filter out numbers which were drawn
	if not each in result_5d_num_only:
		num5d_after_filtered.append(each)
		counter += 1

result_5d_latest = read5d_result_w_draw_no("5D_result.txt")

result_matched = []
for each_num in num5d_after_filtered:
	for each_draw in result_5d_latest:
		if each_num in each_draw:
			result_matched.append(each_draw)

print result_matched

print
print counter





