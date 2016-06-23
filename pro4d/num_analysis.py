"""
Name: num_analysis.py
Objective:  1. Generate numbers from 0000 to 9999
            2. Separate each number to different category - i24, i12, i6, i4
            3. Allow user to get a list of these numbers
            4. Various methods for users to manipulate 4D nums
Params: None
Return: None
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

#run gen_num() and separate num into respective num categorie
def separate_num():
    global list_1
    global list_2
    global list_3
    global list_4
    global list_double
    global clean_list_2

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

def get_list_1():
    # return list of number with no repeating digit
    separate_num()
    return list_1

def get_list_2():
    # return list of number with 2 repeating digits
    separate_num()
    return clean_list_2

def get_list_3():
    # return list of number with 3 repeating digits
    separate_num()
    return list_3

def get_list_4():
    # return list of number with 4 repeating digits
    separate_num()
    return list_4

def get_list_double():
    #return list of number with double double repeating digits
    separate_num()
    return list_double

def check_num_cat(num):
    #return the num cat for given num
    #24 or 12 or 6 or 4
    occur = calc_occurence(num)

    if occur == 1:
        return 24
    elif occur == 2:
        if check_double_double(num):
            return 6
        else:
            return 12
    else:
        return 4

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






###################################
#Below are codes use during testing#
###################################