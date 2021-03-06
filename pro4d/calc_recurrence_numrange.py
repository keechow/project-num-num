"""
Name: calc_recurrence_123.py
Objectives: Calculate recurrence of previously drawn Prize 1,2,3 num based on num range

"""
from file_handler import read
import num_analysis as na

all_num = na.gen_num()
result = read("4D.txt")
latest_result = read("4D-latest.txt")

filtered_result = []    # just want draw no. 1st, 2nd and 3rd
for each in result:
	filtered_result.append([each[0],each[2],each[3],each[4]])

#filtered_result_p1 = []    # prize 1 num
#filtered_result_p2 = []    # prize 2 num
#filtered_result_p3 = []    # prize 3 num

#for each in filtered_result:
#	filtered_result_p1.append([each[0],each[1]])
#	filtered_result_p2.append([each[0],each[2]])
#	filtered_result_p3.append([each[0],each[3]])

# separate nums into respective num range
p1_0k = []
p1_1k = []
p1_2k = []
p1_3k = []
p1_4k = []
p1_5k = []
p1_6k = []
p1_7k = []
p1_8k = []
p1_9k = []
p1_dic = {"0":p1_0k, "1":p1_1k, "2":p1_2k, "3":p1_3k, "4":p1_4k,
		  "5":p1_5k ,"6":p1_6k, "7":p1_7k ,"8":p1_8k, "9":p1_9k}
p1_list = [p1_0k, p1_1k, p1_2k, p1_3k, p1_4k,
		   p1_5k ,p1_6k, p1_7k ,p1_8k, p1_9k]

p2_0k = []
p2_1k = []
p2_2k = []
p2_3k = []
p2_4k = []
p2_5k = []
p2_6k = []
p2_7k = []
p2_8k = []
p2_9k = []
p2_dic = {"0":p2_0k, "1":p2_1k, "2":p2_2k, "3":p2_3k, "4":p2_4k,
		  "5":p2_5k ,"6":p2_6k, "7":p2_7k ,"8":p2_8k, "9":p2_9k}
p2_list = [p2_0k, p2_1k, p2_2k, p2_3k, p2_4k,
		   p2_5k ,p2_6k, p2_7k ,p2_8k, p2_9k]

p3_0k = []
p3_1k = []
p3_2k = []
p3_3k = []
p3_4k = []
p3_5k = []
p3_6k = []
p3_7k = []
p3_8k = []
p3_9k = []
p3_dic = {"0":p3_0k, "1":p3_1k, "2":p3_2k, "3":p3_3k, "4":p3_4k,
		  "5":p3_5k ,"6":p3_6k, "7":p3_7k ,"8":p3_8k, "9":p3_9k}
p3_list = [p3_0k, p3_1k, p3_2k, p3_3k, p3_4k,
		   p3_5k ,p3_6k, p3_7k ,p3_8k, p3_9k]
p123_0k = []
p123_1k = []
p123_2k = []
p123_3k = []
p123_4k = []
p123_5k = []
p123_6k = []
p123_7k = []
p123_8k = []
p123_9k = []
p123_dic = {"0":p123_0k, "1":p123_1k, "2":p123_2k, "3":p123_3k, "4":p123_4k,
		    "5":p123_5k ,"6":p123_6k, "7":p123_7k ,"8":p123_8k, "9":p123_9k}
p123_list = [p123_0k, p123_1k, p123_2k, p123_3k, p123_4k,
		     p123_5k ,p123_6k, p123_7k ,p123_8k, p123_9k]
#[['040792', '0019', '1124', '0592'], ['040892', '0905', '3591', '8690'], ['040992', '4162', '5766', '9514']]

for each_set in filtered_result:
	draw_num = each_set[0]
	p1 = each_set[1]
	p2 = each_set[2]
	p3 = each_set[3]

	p1_dic[p1[0]].append([each_set[0],p1])
	p2_dic[p2[0]].append([each_set[0],p2])
	p3_dic[p3[0]].append([each_set[0],p3])
	p123_dic[p1[0]].append([each_set[0],p1])
	p123_dic[p2[0]].append([each_set[0],p2])
	p123_dic[p3[0]].append([each_set[0],p3])




def recurrence_max_min(num_list):
	#[['040792', '0019'], ['040892', '0905'], ['043692', '0808'], ['047092', '0753']]]
    # 2017-05-18: Something is wrong with this recurrence_max_min function
    # recurrence :  the same num_range occur again
    # no comparisons between current & past num range drawn

	max_counter = 0
	min_counter = 0
	recurrence_rate = []

	idx = 0
	while idx < (len(num_list) - 1):
		current_data = num_list[idx]
		nxt_data = num_list[idx + 1]
		c_draw = int(current_data[0][:4])
		n_draw = int(nxt_data[0][:4])
		diff = n_draw - c_draw
		recurrence_rate.append(diff)
		if diff > max_counter:
			max_counter = diff
		if min_counter > diff or min_counter == 0:
			min_counter = diff
		idx += 1
	return [max_counter,min_counter, recurrence_rate]

r_period = 15

print "For P1:"
ctr = 0
for each in p1_list:
	r_rate =  recurrence_max_min(each)[2]
	recurrence_avg_less = 0
	recurrence_avg_more = 0
	recurrence_avg = 0
	r_custom = 0
	recurrence_count = sum(r_rate)    #sum of all element in recurrence count
	recurrence_average = recurrence_count/len(r_rate)
	for each in r_rate:
		if each <= r_period:
			r_custom += 1
		if each == recurrence_average:
			recurrence_avg += 1
		elif each < recurrence_average:
			recurrence_avg_less += 1
		else:
			recurrence_avg_more += 1
	print "Current num_range: ", ctr
	print "Average : ", recurrence_average
	print "Number of recurrence period less than average: ", recurrence_avg_less
	print "Number of recurrence period more than average: ", recurrence_avg_more
	print "Number of recurrence period equal to average: ", recurrence_avg
	print "No. of recurrence period less than 12: ", r_custom
	print "Total: ", len(r_rate)
	print "Percentage: ", (float(100*r_custom)/len(r_rate))

	print "================================================================"
	ctr += 1
print
print
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print

print "For P2: "
ctr = 0
for each in p2_list:

	r_rate =  recurrence_max_min(each)[2]
	recurrence_avg_less = 0
	recurrence_avg_more = 0
	recurrence_avg = 0
	r_custom = 0
	recurrence_count = sum(r_rate)    #sum of all element in recurrence count
	recurrence_average = recurrence_count/len(r_rate)
	for each in r_rate:
		if each <= r_period:
			r_custom += 1
		if each == recurrence_average:
			recurrence_avg += 1
		elif each < recurrence_average:
			recurrence_avg_less += 1
		else:
			recurrence_avg_more += 1
	print "Current num_range: ", ctr
	print "Average : ", recurrence_average
	print "Number of recurrence period less than average: ", recurrence_avg_less
	print "Number of recurrence period more than average: ", recurrence_avg_more
	print "Number of recurrence period equal to average: ", recurrence_avg
	print "No. of recurrence period less than 12: ", r_custom
	print "Total: ", len(r_rate)
	print "Percentage: ", (float(100*r_custom)/len(r_rate))
	print "================================================================"
	ctr += 1
print
print
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print

print "For P3: "
ctr = 0
for each in p3_list:
	r_rate =  recurrence_max_min(each)[2]
	recurrence_avg_less = 0
	recurrence_avg_more = 0
	recurrence_avg = 0
	r_custom = 0
	recurrence_count = sum(r_rate)    #sum of all element in recurrence count
	recurrence_average = recurrence_count/len(r_rate)
	for each in r_rate:
		if each <= r_period:
			r_custom += 1
		if each == recurrence_average:
			recurrence_avg += 1
		elif each < recurrence_average:
			recurrence_avg_less += 1
		else:
			recurrence_avg_more += 1
	print "Current num_range: ", ctr
	print "Average : ", recurrence_average
	print "Number of recurrence period less than average: ", recurrence_avg_less
	print "Number of recurrence period more than average: ", recurrence_avg_more
	print "Number of recurrence period equal to average: ", recurrence_avg
	print "No. of recurrence period less than 1l2: ", r_custom
	print "Total: ", len(r_rate)
	print "Percentage: ", (float(100*r_custom)/len(r_rate))

	print "================================================================"
	ctr += 1
print
print
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print

print "For P123: "
ctr = 0
for each in p123_list:
	r_rate =  recurrence_max_min(each)[2]
	recurrence_avg_less = 0
	recurrence_avg_more = 0
	recurrence_avg = 0
	r_custom = 0
	recurrence_count = sum(r_rate)    #sum of all element in recurrence count
	recurrence_average = recurrence_count/len(r_rate)
	for each in r_rate:
		if each < 2:
			r_custom += 1
		if each == recurrence_average:
			recurrence_avg += 1
		elif each < recurrence_average:
			recurrence_avg_less += 1
		else:
			recurrence_avg_more += 1
	print "Current num_range: ", ctr
	print "Average : ", recurrence_average
	print "Number of recurrence period less than average: ", recurrence_avg_less
	print "Number of recurrence period more than average: ", recurrence_avg_more
	print "Number of recurrence period equal to average: ", recurrence_avg
	print "No. of recurrence period less than 6: ", r_custom
	print "Total: ", len(r_rate)
	print "Percentage: ", (float(r_custom)/len(r_rate))
	print "================================================================"
	ctr += 1
print
print
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print "======================================================================================"
print




# generate all_4d_num

# compare each num from all_4d_num with result
# store each occurrence in prize1_list, prize2_list and prize3_list