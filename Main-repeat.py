__author__ = 'keechow'
# the idea is to monitor the pattern of occurence for one given number
# if numbers were drawn randomly, the possibility for each number is the same for all number
# check for numbers that were drawn periodically and numbers that weren't drawn for some time

# for 5D numbers, there are 3 prizes: 1st, 2nd, 3rd.
# create a number generator to generate 00000 to 99999
# convert num to str, append in to separate list
# match draw num with element[0] in the list, if matched, append the date

# example of data stream:   040792,19920506,26094,21292,47699

from file_handler import read4d_result
from file_handler import read5d_result
from file_handler import read6d_result
from separate_by_month import separate_4d
from separate_by_month import separate_5d
from separate_by_month import separate_6d

def num_generator_5d():
	#generate 00000 to 99999
    return_list = []
    counter = 0
    while counter < 100000:
		lst = []
		str_num = str(counter)
		if len(str_num) < 5:
			while len(str_num) < 5:
				str_num = "0" + str_num
		lst.append(str_num)
		return_list.append(lst)
		counter += 1
    return return_list

def match(num_list, data):
	# takes in result data in form ["draw num", "draw date", "1st","2nd","3rd"]
	# takes in the 100k num_list to work with
	# append draw num into 100k num list accordance to num drawn from data


	return_list = list(num_list)

	for num_drawn in data[2:]:
		position = int(num_drawn)
		return_list[position].append(data[0])

	return return_list

from file_handler import read5d_result_w_draw_no

data_5d = read5d_result_w_draw_no("5D.txt")

result_list = num_generator_5d()

for each_draw in data_5d:
	draw_no = each_draw[0]
	num_drawn = each_draw[2:]
	for each_num in num_drawn:
		position = int(each_num)
		result_list[position].append(draw_no)

for each_num in result_list:
	if len(each_num) > 1:
		print each_num
		print


