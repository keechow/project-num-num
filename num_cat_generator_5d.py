__author__ = 'keechow'

"""
Generate 5D numbers, classify them into their categories and count.
use .count()

"""
num5d_list = []
counter = 0
while counter < 100000:
	str_num = str(counter)
	if len(str_num) < 5:
		while len(str_num) < 5:
			str_num = "0" + str_num
	num5d_list.append(str_num)
	counter += 1

i1 = []
i5 = []
i10 = []
i20 = []
i30 = []
i60 = []
i120 = []

for each_num in num5d_list:
	str_int_dict = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
	for each in str_int_dict:
		str_int_dict[each] = each_num.count(each)
	#count occurrences of each digit

	max_count = max(str_int_dict, key=str_int_dict.get)
	#get the max count, this is to detect repeated digits

	if max_count == 5:    #5 same digits
		i1.append(each_num)
	elif max_count == 4:    #4 same digits + 1 different digit
		i5.append(each_num)
	elif max_count == 3:    #3 same digits
		if 2 in str_int_dict.values():
			i10.append(each_num)    # + 2 same digits
		else:
			i20.append(each_num)    # + 2 different digits
	elif max_count == 2:    #2 same digits
		if str_int_dict.values().count(2) == 2:    #count the values of 2 in dit
			i30.append(each_num)    # + 2 same digits + 1 different digit
		else:
			i60.append(each_num)    # + 3 different digits
	else:
		i120.append(each_num)    #5 different digits

print len(i1)
print
print len(i5)
print
print len(i10)
print
print len(i20)
print
print len(i30)
print
print len(i60)
print
print len(i120)