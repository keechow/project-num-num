"""
Name: num_range_consecutive.py
Objectives: Investigate the possibility of drawing consecutive num_range

"""
from file_handler import read
import num_analysis as na

def num_range_p123():
	result = read("4D.txt")
	p123_result = []
# just want draw no. 1st, 2nd and 3rd
# example of data stream from 4D.txt:
# 040792,19920506,0019,1124,0592,0950,2479,7139,3114,4609,7836,8981,4465,6114,5301,5311,1949,1606 3775,6226,1271,7455,7227,9258,0407
# just want draw no. 1st, 2nd and 3rd
	p1 = []
	p2 = []
	p3 = []
	for each in result:
		p123_result.append([each[0],each[2],each[3],each[4]])
		p1.append([each[0],each[2]])
		p2.append([each[0],each[3]])
		p3.append([each[0],each[4]])

	return [p1,p2,p3,p123_result]

def check_num_csq(c_num, n_num):
	num_lst = [["1","9"],["0","2"],["1","3"],["2","4"],["3","5"],
			   ["4","6"],["5","7"],["6","8"],["7","9"],["0","8"]]
	if n_num in num_lst[int(c_num)]:
		return True
	else:
		return False

def csq_num_ctr_one(num_list):
	# num_list : [['040792', '0019'], ['040892', '0905'], ['043692', '0808'],...]
	idx = 0
	csq_num_count = 0
	while idx < (len(num_list) - 1):
		c_num_range = num_list[idx][1][0]
		n_num_range = num_list[idx + 1][1][0]
		if check_num_csq(c_num_range,n_num_range):
			csq_num_count += 1
		idx += 1
	return csq_num_count

def csq_num_ctr_all(num_list):
	# [['040792', '0019', '1124', '0592'], ['040892', '1111', '3591', '8690'],...]
	idx = 0
	p1_ctr = 0
	p2_ctr = 0
	p3_ctr = 0
	while idx < (len(num_list)-1):
		p1_c_n_r = num_list[idx][1][0]
		p2_c_n_r = num_list[idx][2][0]
		p3_c_n_r = num_list[idx][3][0]

		p1_nx_n_r = num_list[idx+1][1][0]
		p2_nx_n_r = num_list[idx+1][2][0]
		p3_nx_n_r = num_list[idx+1][3][0]

		if check_num_csq(p1_c_n_r, p3_nx_n_r):
			p1_ctr += 1
		if check_num_csq(p2_c_n_r, p3_nx_n_r):
			p2_ctr += 1
		if check_num_csq(p3_c_n_r, p2_nx_n_r):
			p3_ctr += 1
		idx += 1
	return [p1_ctr,p2_ctr,p3_ctr]






n_r_p1 = num_range_p123()[0]   # all num range P1
n_r_p2 = num_range_p123()[1]    # all num range P2
n_r_p3 = num_range_p123()[2]    # all num range P3
n_r_p123 = num_range_p123()[3]    # all num range P123
print csq_num_ctr_all(n_r_p123)
print
print "Length: ", len(n_r_p123)
"""
print "P1: "
print len(n_r_p1)
print csq_num_ctr(n_r_p1)
print float(csq_num_ctr(n_r_p1))/len(n_r_p1)
print
print

print "P21: "
print len(n_r_p2)
print csq_num_ctr(n_r_p2)
print float(csq_num_ctr(n_r_p2))/len(n_r_p2)
print
print
print "P3: "
print len(n_r_p3)
print csq_num_ctr(n_r_p3)
print float(csq_num_ctr(n_r_p3))/len(n_r_p3)
print
print

"""

