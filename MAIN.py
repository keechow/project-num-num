__author__ = 'keechow'

from file_handler import read4d_result
from file_handler import read5d_result
from file_handler import read6d_result
from separate_by_month import separate_4d
from separate_by_month import separate_5d
from separate_by_month import separate_6d

data_4d = read4d_result("4D.txt")
data_5d = read5d_result("5D.txt")
data_6d = read6d_result("6D.txt")

data_4d_by_month = separate_4d(data_4d)
data_5d_by_month = separate_5d(data_5d)
data_6d_by_month = separate_6d(data_6d)

data_5d_jan = data_5d_by_month[0]
print data_5d_jan[0]

#['19930103', '69610', '46920', '83409']

def num_range_counter(data):
	first_ctr = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0,"8":0, "9":0}
	second_ctr = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0,"8":0, "9":0}
	third_ctr = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0,"8":0, "9":0}

	for each_data in data:
		for each_prize in each_data[1:]:

		first = each_data[1] #1st prize num is the second element
		second = each_data[2]
		third = each_data[3]

		first digit = first[0]
		second_digit = second[0]
		third_
		digit = each_data[1]
		if digit[0] in range_counter:
			range_counter[digit] += 1
	return range_counter

data_5d_jan_count = num_range_counter(data_5d_jan)

print data_5d_jan_count

print "\n\n\n============== SUCCESSFULLY EXECUTED ================"
print "============== SUCCESSFULLY EXECUTED ================"
print "============== SUCCESSFULLY EXECUTED ================"