__author__ = 'keechow'
# the idea is to monitor the pattern of occurence for one given number
# if numbers were drawn randomly, the possibility for each number is the same for all number
# check for numbers that were drawn periodically and numbers that weren't drawn for some time

# for 5D numbers, there are 3 prizes: 1st, 2nd, 3rd.
# create a number generator to generate 00000 to 99999
# convert num to str, append in to separate list
# match draw num with element[0] in the list, if matched, append the date

def num_generator_5d():
	#generate 00000 to 99999
    return_list = []
    counter = 0
    while counter < 100000:
		str_num = str(counter)
		while len(str_num) < 6:
			str_num = "0" + str_num
		return_list.append(str_num)
		counter += 1
    return return_list

num = num_generator_5d()

print num

