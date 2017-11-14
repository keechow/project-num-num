def counter_list_3draw(drawSet_data):
	# params: list of data containing draw set pattern
	# count each draw set pattern
	# return a list containing count for each draw set pattern in respective position
	# e.g. element [203] correspond to draw set pattern 203
	return_counter_list = []
	for each in range(1000):
		return_counter_list.append(0)

	for each in drawSet_data:
		int_each = int(each)
		count = return_counter_list[int_each] + 1
		return_counter_list[int_each] = count

	return return_counter_list

