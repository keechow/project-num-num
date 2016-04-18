"""
Name: num_range_count.py
Author: echo.telion@gmail.com
Objective: Calculate the occurrence for according to number range, 00000-09999, 10000-19999,...,90000-99999
Input: List of result extracted from txt file
Output: List of count sorted with from 0 to 9

"""
def num_range_counter(data):
	ctr= {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0,"8":0, "9":0}
	first_digit = data[0]
	if first_digit in ctr:
		ctr[first_digit] += 1
	return ctr

def count5D_numrange(data):

	ctr1= {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0,"8":0, "9":0}
	ctr2= {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0,"8":0, "9":0}
	ctr3= {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0,"8":0, "9":0}
	    #store counts for each digit drawn for prize 1,2,3

	for each_data_set in data:
		result1 = each_data_set[1] #prize 1
		result2 = each_data_set[2] #prize 2
		result3 = each_data_set[3] #prize 3

		result_ctr_dict1 = num_range_counter(result1)
		result_ctr_dict2 = num_range_counter(result2)
		result_ctr_dict3 = num_range_counter(result3)

		for each_num_ctr in result_ctr_dict1:
			if each_num_ctr in ctr1:
				ctr1[each_num_ctr] += result_ctr_dict1[each_num_ctr]

		for each_num_ctr in result_ctr_dict2:
			if each_num_ctr in ctr2:
				ctr2[each_num_ctr] += result_ctr_dict2[each_num_ctr]

		for each_num_ctr in result_ctr_dict3:
			if each_num_ctr in ctr3:
				ctr3[each_num_ctr] += result_ctr_dict3[each_num_ctr]

	prize1_count = [0,0,0,0,0,0,0,0,0,0]
	prize2_count = [0,0,0,0,0,0,0,0,0,0]
	prize3_count = [0,0,0,0,0,0,0,0,0,0]

	for each in ctr1:
		position = int(each)
		prize1_count[position] = ctr1[each]

	for each in ctr2:
		position = int(each)
		prize2_count[position] = ctr2[each]

	for each in ctr3:
		position = int(each)
		prize3_count[position] = ctr3[each]

	return [prize1_count,prize2_count,prize3_count]


