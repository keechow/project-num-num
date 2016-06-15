__author__ = 'keechow'
# the idea is to monitor the pattern of occurence for one given number
# if numbers were drawn randomly, the possibility for each number is the same for all number
# check for numbers that were drawn periodically and numbers that weren't drawn for some time

# for 5D numbers, there are 3 prizes: 1st, 2nd, 3rd.
# create a number generator to generate 00000 to 99999
# convert num to str, append in to separate list
# match draw num with element[0] in the list, if matched, append the date

# example of data stream:   040792,19920506,26094,21292,47699

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

file_5d = open("5D_result_repeat.txt", 'w')
file_5d0 = open("5D_result_repeat0.txt", 'w')
file_5d1 = open("5D_result_repeat1.txt", 'w')
file_5d2 = open("5D_result_repeat2.txt", 'w')
file_5d3 = open("5D_result_repeat3.txt", 'w')
file_5d4 = open("5D_result_repeat4.txt", 'w')
file_5d5 = open("5D_result_repeat5.txt", 'w')
file_5d6 = open("5D_result_repeat6.txt", 'w')
file_5d7 = open("5D_result_repeat7.txt", 'w')
file_5d8 = open("5D_result_repeat8.txt", 'w')
file_5d9 = open("5D_result_repeat9.txt", 'w')



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
		file_5d.write(str(each_num))
		file_5d.write("\n")

position1 = 10000
position2 = 20000
position3 = 30000
position4 = 40000
position5 = 50000
position6 = 60000
position7 = 70000
position8 = 80000
position9 = 90000

result0k = result_list[:position1]
result10k = result_list[position1:position2]
result20k = result_list[position2:position3]
result30k = result_list[position3:position4]
result40k = result_list[position4:position5]
result50k = result_list[position5:position6]
result60k = result_list[position6:position7]
result70k = result_list[position7:position8]
result80k = result_list[position8:position9]
result90k = result_list[position9:]

total_count = 0
counter = 0
for each_num in result0k:
	if len(each_num) > 1:
		counter +=1
		file_5d0.write(str(each_num))
		file_5d0.write("\n")
print "Result 00000 - 99999: " + str(counter)
print
total_count+= counter

counter = 0
for each_num in result10k:
	if len(each_num) > 1:
		counter += 1
		file_5d1.write(str(each_num))
		file_5d1.write("\n")
print "Result 10000 - 19999: " + str(counter)
print
total_count+= counter

counter = 0
for each_num in result20k:
	if len(each_num) > 1:
		counter += 1
		file_5d2.write(str(each_num))
		file_5d2.write("\n")
print "Result 20000 - 29999: " + str(counter)
print
total_count+= counter

counter = 0
for each_num in result30k:
	if len(each_num) > 1:
		counter += 1
		file_5d3.write(str(each_num))
		file_5d3.write("\n")
print "Result 30000 - 39999: " + str(counter)
print
total_count+= counter

counter = 0
for each_num in result40k:
	if len(each_num) > 1:
		counter += 1
		file_5d4.write(str(each_num))
		file_5d4.write("\n")
print "Result 40000 - 49999: " + str(counter)
print
total_count+= counter

counter = 0
for each_num in result50k:
	if len(each_num) > 1:
		counter += 1
		file_5d5.write(str(each_num))
		file_5d5.write("\n")
print "Result 50000 - 59999: " + str(counter)
print
total_count+= counter

counter = 0
for each_num in result60k:
	if len(each_num) > 1:
		counter += 1
		file_5d6.write(str(each_num))
		file_5d6.write("\n")
print "Result 60000 - 69999: " + str(counter)
print
total_count+= counter

counter = 0
for each_num in result70k:
	if len(each_num) > 1:
		counter += 1
		file_5d7.write(str(each_num))
		file_5d7.write("\n")
print "Result 70000 - 79999: " + str(counter)
print
total_count+= counter

counter = 0
for each_num in result80k:
	if len(each_num) > 1:
		counter += 1
		file_5d8.write(str(each_num))
		file_5d8.write("\n")
print "Result 80000 - 89999: " + str(counter)
print
total_count+= counter

counter = 0
for each_num in result90k:
	if len(each_num) > 1:
		counter += 1
		file_5d9.write(str(each_num))
		file_5d9.write("\n")
print "Result 90000 - 99999: " + str(counter)
print
total_count+= counter

print "Total Count:  " + str(total_count)