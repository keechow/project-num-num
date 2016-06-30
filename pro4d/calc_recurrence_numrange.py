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

filtered_result_p1 = []    # prize 1 num
filtered_result_p2 = []    # prize 2 num
filtered_result_p3 = []    # prize 3 num

for each in filtered_result:
	filtered_result_p1.append([each[0],each[1]])
	filtered_result_p2.append([each[0],each[2]])
	filtered_result_p3.append([each[0],each[3]])

print filtered_result_p1

num_0 = all_num[:1000]
num_1 = all_num[1000:2000]
num_2 = all_num[2000:3000]
num_3 = all_num[3000:4000]
num_4 = all_num[4000:5000]
num_5 = all_num[5000:6000]
num_6 = all_num[6000:7000]
num_7 = all_num[7000:8000]
num_8 = all_num[8000:9000]
num_9 = all_num[9000:]


# generate all_4d_num

# compare each num from all_4d_num with result
# store each occurrence in prize1_list, prize2_list and prize3_list