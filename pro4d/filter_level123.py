"""
Name: filter_level123.py
Objective: Produce a list of wanted nums
Input: CNR, CPCAT
Author: echo.telion@gmail.com

"""
##### IMPORT THIS IMPORT THAT #####
import num_analysis as na
	#i24 = na.get_list_1()
	#i12 = na.get_list_2()
	#i6 = na.get_list_double()
	#i4 = na.get_list_3()
	#i1 = na.get_list_4()
from file_handler import read
##################################

def filter_level123(result_position):
	##############################################################
	###====================   L1 Filter  ======================###
	##############################################################

	# Filter out : i1_num, i4_num, seq_num

	str_list_wanted_num_l1 = []

	str_list_10k_num = na.gen_num()
	#['0000', '0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009', '0010',

	str_list_seq_num = na.seq_num()
	# ["0123","1234","2345","3456","4567","5678","6789","9876","8765","7654","6543","5432","4321","3210"]

	str_list_i1_num = na.get_list_4()
	#['0000', '1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888', '9999']

	str_list_i4_num = na.get_list_3()
	#['0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009', '0010',

	l1_no_list = str_list_seq_num + str_list_i1_num + str_list_i4_num

	for each in str_list_10k_num:
		if not each in l1_no_list:
			str_list_wanted_num_l1.append(each)

	##############################################################
	###====================   L2 Filter  ======================###
	##############################################################

	# Filter out : recently drawn numbers, csq num range
	# 1. Get numbers drawn for the past 3 years
	#	- read result txt file
	#	- read result from year 2016, 2015, 2014

	result = read("4D.txt")

	drawn_p123num_past3yr = []	# list of num drawn for the past 3 years
	for each_draw in result[(result_position-535):result_position]:	#178 or 179 draws each year. 3years = 535 draws
		drawn_p123num_past3yr.append(each_draw[2])	#num pcat1
		drawn_p123num_past3yr.append(each_draw[3])	#num pcat2
		drawn_p123num_past3yr.append(each_draw[4])	#num pcat3

	# 2. Parse cnr.
	# 3. Determine nnr.
	last_draw_p1_nr = result[result_position][2][0]
	int_last_draw_p1_nr = int(last_draw_p1_nr)
	int_csq_p1_nr = int_last_draw_p1_nr + 1
	if int_csq_p1_nr > 9:
		int_csq_p1_nr = 0
	str_csq_p1_nr = str(int_csq_p1_nr)

	str_list_csq_p1_nr_num = na.gen_num_for_nr(str_csq_p1_nr)

	# 4. L2 Filtering: continue using str_list_wanted_num_l1

	str_list_wanted_num_l2 = []

	for each in str_list_wanted_num_l1:
		if not each[0] == str_csq_p1_nr and not each in drawn_p123num_past3yr:
			str_list_wanted_num_l2.append(each)

	l2_no_list = drawn_p123num_past3yr + str_list_csq_p1_nr_num

	##############################################################
	###====================   L3 Filter  ======================###
	##############################################################

	#	1. Read cnr and cpcat from result data file
	#	2. Get filter code based on cnr and cpcat
	#	3. Produce no list based on filter code

	l3_m1_filter_code = ["1162","1189", "2149", "2164", "3119", "3128", "3132", "3147", "3167", "1237", "1265", "1274", "1296", "2206", "2244", "2266", "3219", "3219", "3228", "3232", "3244", "3267", "1314", "1390", "2336", "2384", "3302", "3347", "1465", "1490", "2464", "2474", "2455", "3495"]
	#[cpcat npcat cnr nnr]

	l3_m2_filter_code = ["11724", "11406", "21424", "21606", "31824", "12524", "12906", "22206", "32724", "13404", "23606", "23724", "33824", "14524", "14906"]	#[cpcat npcat cnr nncat]

	l3_m3_filter_code = ["11118", "13123", "15111", "15114", "19113", "21115", "21125", "22118", "23121", "25118", "26112", "26117", "27116", "27121", "27122", "29125", "31114", "31126", "33125", "35116", "39123", "11211", "11220", "11222", "14216", "16215", "16223", "19225", "21215", "21217", "21220", "23214", "25214", "25216", "27212", "27213", "27215", "27226", "29226", "31226", "33216", "33218", "33224", "37212", "39215", "11315", "11321", "11322", "11327", "13311", "13324", "15316", "15323", "15325", "15327", "17318", "19323", "23327", "27312", "27324", "27325", "29324", "31313", "31322", "31326", "35323", "35326", "39316", "11418", "11422", "11428", "15408", "15423", "17409", "19408", "27422", "27428", "31407", "31426", "31428", "33407", "35408", "35409", "39415", "39416"]
	#[cpcat cnr npcat nnsum]

	l3_npcat1_no_num_list = []
	l3_npcat2_no_num_list = []
	l3_npcat3_no_num_list = []
	l3_npcat4_no_num_list = []

	pcat_dict = {"24":na.get_list_1(), "12":na.get_list_2(), "06":na.get_list_double(), "04":na.get_list_3(), "01":na.get_list_1()}

	l3_npcat_dict = {"1":l3_npcat1_no_num_list, "2":l3_npcat2_no_num_list, "3":l3_npcat3_no_num_list, "4":l3_npcat4_no_num_list}

	cnr_dict = {"1":result[result_position][2][0], "2":result[result_position][3][0], "3":result[result_position][4][0]}
			#[cnr_pcat1, cnr_pcat2, cnr_pcat3]



		# read each code from m filter
		# determine cpcat, cnr, npcat, nnr/nncat/nnsum
		# match cpcat and cnr
		# generate no num from nnr/nncat/nnsum
		# identify which list to append to using npcat and npcat_dict

	for each in l3_m1_filter_code:
		# l3_m1_filter_code = ["1162","1189", "2149", "2164",
		# [cpcat npcat cnr nnr]
		# 1. check if cnr_code and cpcat_code matches with cnr and cpcat from result data
		# 2. generate unwanted num (nr_list) using nnr_code
		# 3. append all num into l3 no num list, depending on npcat_code

		cpcat_code = each[0]
		npcat_code = each[1]
		cnr_code = each[2]
		nnr_code = each[3]

		if cnr_code == cnr_dict[cpcat_code]:
			nr_list = na.gen_num_for_nr(nnr_code)
			for each in nr_list:
				l3_npcat_dict[npcat_code].append(each)

	for each in l3_m2_filter_code:
		# l3_m2_filter_code = ["11724", "11406", "21424",
		# [cpcat npcat cnr nncat]
		# 1. check if cnr_code and cpcat_code matches with cnr and cpcat from result data
		# 2. generate unwanted num (nncat_list) using nnr_code
		# 3. append all num into l3 no num list, depending on npcat_code

		cpcat_code = each[0]
		npcat_code = each[1]
		cnr_code = each[2]
		nncat_code = each[3:]

		if cnr_code == cnr_dict[cpcat_code]:
			nncat_list = pcat_dict[nncat_code]
			for each in nncat_list:
				l3_npcat_dict[npcat_code].append(each)

	for each in l3_m3_filter_code:
		# l3_m3_filter_code = ["11118", "13123", "15111"
		#[cpcat cnr npcat nnsum]
		# 1. check if cnr_code and cpcat_code matches with cnr and cpcat from result data
		# 2. generate unwanted num (nnsum_list) using nnsum_code
		# 3. append all num into l3 no num list, depending on npcat_code

		cpcat_code = each[0]
		npcat_code = each[2]
		cnr_code = each[1]
		nnsum_code = each[3:]

		if cnr_code == cnr_dict[cpcat_code]:
			nnsum_list = na.gen_num_for_nsum(nnsum_code)
			for each in nnsum_list:
				l3_npcat_dict[npcat_code].append(each)

		# each list contains duplicates - clean them up
	l3_npcat1_no_num_list_clean = list(set(l3_npcat1_no_num_list))
	l3_npcat2_no_num_list_clean = list(set(l3_npcat2_no_num_list))
	l3_npcat3_no_num_list_clean = list(set(l3_npcat3_no_num_list))

		# filter str_list_wanted_num_l2 to produce str_list_wanted_num_l3
		# only filter out l3_npcat1_no_num_list_clean

	str_list_wanted_num_l3 = []
	for each in str_list_wanted_num_l2:
		if not each in l3_npcat1_no_num_list_clean:
			str_list_wanted_num_l3.append(each)


	# combine l1_no_list, l2_no_list and l3_npcat1_no_num_list_clean
	# use set to identify elements that intersect between all 3 lists
	# append matched nums in all 3 lists into l123_no_list


	str_list_l123_no_num_type1 = list(set(l1_no_list) & set(l2_no_list) & set(l3_npcat1_no_num_list_clean))

	str_list_l123_no_num_type2 = l1_no_list + list(set(l2_no_list) & set(l3_npcat1_no_num_list_clean))

	str_list_l123_no_num_type3 = l1_no_list + l2_no_list + l3_npcat1_no_num_list_clean

	# use set to remove no_nums from 10k 4D num
	# s.difference(t)	new set with elements in s but not in t
	# s - t

	str_list_final_wanted_num = list(set(str_list_10k_num) - set(str_list_l123_no_num_type3))
	print "len(str_list_l123_no_num_type3) =  " + str(len(str_list_l123_no_num_type3))
	print "str_list_final_wanted_num: " + str(len(str_list_final_wanted_num))
	return str_list_final_wanted_num



result_position = 3991
result = read("4D.txt")
result_counter = 0
missed_counter = 0
hit_draw_num_list = []
miss_draw_num_list = []
while result_position < (len(result)-1):
	print
	print "+++++++++++++++++++++++++++++++++++++"
	print "Current Position: ", result_position

	wanted_num_list = filter_level123(result_position)
	nxt_p1num = result[result_position+1][2]
	if nxt_p1num in wanted_num_list:
		#print
		#print "Wanted List Len: " + str(len(wanted_num_list))
		#print "Current Position: " + str(result_position)
		#print "Current P1 num: " + str(result[result_position][2])
		#print "Next P1 num: " + str(result[result_position+1][2])
		#print
		#print "===================================================================="
		result_counter += 1
		hit_draw_num_list.append(str(result_position))
		print "HIT HIT HIT"
		print "========================================================================"
	else:
		missed_counter += 1
		miss_draw_num_list.append(str(result_position))
		print "MISSED MISSED"
		print "========================================================================"
	result_position += 1


#============ TESTING GROUND=============#

print "Result len: ", len(result)

print "Hit Counter: ", result_counter

print "Missed Counter: ", missed_counter

print
print
print "Hit Num Draw: "
print hit_draw_num_list
print
print miss_draw_num_list
"""
print len(str_list_10k_num)
print len(str_list_wanted_num_l1)
print len(str_list_wanted_num_l2)
print len(str_list_wanted_num_l3)
"""

print
print
print
print
print "###############################################################"
print "#########  COMPLETED  ###################  COMPLETED  ##########"
print "################################################################"



