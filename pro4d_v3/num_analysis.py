"""
Name: num_analysis.py
List of functions:
    1) str_num(): take an integer return a 4 digit string
    2) gen_num(): generate a string list containing element 0001 to 9999
    3) calc_occurence(): calculate how many times a num is repeated
    4) check_double_double(): check if given number is  double-double
    5) separate_num(): run gen_num() and separate num into respective num category

Author: Project Echo Telion <echo.telion@gmail.com>

"""

list_1 = []    #list containing numbers with no repeating digit
list_2 = []    #list containing numbers with 2 repeating digits
list_3 = []    #list containing numbers with 3 repeating digits
list_4 = []    #list containing numbers with 4 repeating digits
list_double = []    #list containing numbers with 2 pairs of digits
clean_list_2 = []    #list_2 with overlapping elements from list_double removed

#take an integer return a 4 digit string.
def str_num(num):
    str_num = str(num)
    while len(str_num) < 4:
        str_num = "0" + str_num
    return str_num

#generate a string list containing element 0001 to 9999
def gen_num():
    num = 0
    str_num_list = []
    while num < 10000:
        element_ = str_num(num)
        str_num_list.append(element_)
        num += 1
    return str_num_list

#calculate how many times a num is repeated
def calc_occurence(str_num):
    check_digit = ['0','1','2','3','4','5','6','7','8','9']
    occurence = 1
    for each in check_digit:
        count = str_num.count(each)
        if count > occurence:
            occurence = count
    return occurence

#check if given number is  double-double
def check_double_double(str_num):
    check_digit = ['0','1','2','3','4','5','6','7','8','9']
    for each in check_digit:
        count = str_num.count(each)
        if count == 2:
            for num in check_digit:
                count2 = str_num.count(num)
                if count2 == 2 and num != each:
                    return True
    return False

#run gen_num() and separate num into respective num category
def separate_num():
    global list_1
    global list_2
    global list_3
    global list_4
    global list_double
    global clean_list_2

    del list_1[:]
    del list_2[:]
    del list_3[:]
    del list_4[:]
    del list_double[:]
    del clean_list_2[:]

    num_list = gen_num()
    for each in num_list:
        occur = calc_occurence(each)
        if occur == 1:
            list_1.append(each)
        elif occur == 2:
            list_2.append(each)
        elif occur == 3:
            list_3.append(each)
        else:
            list_4.append(each)

    for each in list_2:
        if check_double_double(each):
            list_double.append(each)

    #there are same number in list_2 and list_double. we want to remove these numbers from list_2
    set_list2 = set(list_2)
    set_list_double = set(list_double)
    clean_list_2 = list(set_list2.difference(set_list_double))

# return list of number with no repeating digit
def get_list_1():
    separate_num()
    return list_1

# return list of number with 2 repeating digits
def get_list_2():
    separate_num()
    return clean_list_2

# return list of number with 3 repeating digits
def get_list_3():
    separate_num()
    return list_3

# return list of number with 4 repeating digits
def get_list_4():
    separate_num()
    return list_4

#return list of number with double double repeating digits
def get_list_double():
    separate_num()
    return list_double

#return the num cat for given num (24 or 12 or 6 or 4)
def check_num_cat(num):
    occur = calc_occurence(num)

    if occur == 1:
        return 24
    elif occur == 2:
        if check_double_double(num):
            return 6
        else:
            return 12
    elif occur == 3:
        return 4
    else:
        return 1

#return a list of sequential numbers, e.g. 1234, 4567, 6789
def seq_num():
    return (["0123","1234","2345","3456","4567",
             "5678","6789","9876","8765","7654",
             "6543","5432","4321","3210"])


def clean_duplicate(num_list):
	return_list = []
	duplicate = set()
	for each_num in num_list:
		if each_num not in duplicate:
			return_list.append(each_num)
			duplicate.add(each_num)
	return return_list

def identify_n_range(num):
	#type(num) = str, eg: 4566
	return num[0]

def identify_odd_even(num):
    if (num % 2) > 0:
        return "Odd"
    else:
        return "Even"

def identify_n_sum(num):

    total = 0
    for each in num:
        total += int(each)
    return total

def check_num_csq(c_num, n_num):
	num_lst = [["1","9"],["0","2"],["1","3"],["2","4"],["3","5"],
			   ["4","6"],["5","7"],["6","8"],["7","9"],["0","8"]]
	if n_num in num_lst[int(c_num)]:
		return True
	else:
		return False

def num_sum_list():
	#generating a list containing numbers from 0000 to 9999
	ctr = 0
	sum_num_list = []
	while ctr < 37:    # the max sum for 0000 to 9999 = 36
		sum_num_list.append([])
		ctr += 1

	int_num_list = []
	counter = 0
	while counter <10000:
		int_num_list.append(counter)
		counter += 1
	for each_num in int_num_list:
		sum_of_num = calc_digit_sum(each_num)
		str_each_num = str(each_num)
		while len(str_each_num) < 4:
			str_each_num = "0" + str_each_num
		sum_num_list[sum_of_num].append(str_each_num)
	return sum_num_list

def calc_digit_sum(number):
    #return the sum of all digits in number input
	return_sum = 0
	str_number = str(number)
	for each_digit in str_number:
		return_sum += int(each_digit)
	return return_sum

def gen_num_for_nr(numrange):
	# produce a list of 4D num for range entered
	# e.g. input = 3, output: ["3000", "3001",...,"3999"]

	output_list = []
	for num in range(1000):
		num_str = str(num)
		while len(num_str) < 3:
			num_str = "0" + num_str
		output_list.append(numrange + num_str)

	return output_list

def gen_num_for_nsum(nsum):
	# produce a list of 4D num for the nsum entered
	nsum_int = int(nsum)
	nsum_all = num_sum_list()
	return nsum_all[nsum_int]







###################################
#Below are codes use during testing#


##################################
