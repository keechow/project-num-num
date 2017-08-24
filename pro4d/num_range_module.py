"""
name: num_range_module.py
objective: take in result data file, parse data into separate list according to prize_cat and num_range
returns: [p1_list, p2_list, p3_list, p123_list]
author: echo.telion@gmail.com

"""
def num_range_p123():
	result = read("4D.txt")
	filtered_result = []    # just want draw no. 1st, 2nd and 3rd
# example of data stream from 4D.txt:
# 040792,19920506,0019,1124,0592,0950,2479,7139,3114,4609,7836,8981,4465,6114,5301,5311,1949,1606 3775,6226,1271,7455,7227,9258,0407
# just want draw no. 1st, 2nd and 3rd

	for each in result:
		filtered_result.append([each[0],each[2],each[3],each[4]])

# separate filtered result in accordance to Prize type and num range
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
			   p1_5k ,p1_6k, p1_7k ,p1_8k, p1_9k]    # all num range for p1

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
			   p2_5k ,p2_6k, p2_7k ,p2_8k, p2_9k]       # all num range for p2

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
			   p3_5k ,p3_6k, p3_7k ,p3_8k, p3_9k]    # all num range for p3

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
				 p123_5k ,p123_6k, p123_7k ,p123_8k, p123_9k]    # all num range for p123

	for each_set in filtered_result:
		p1 = each_set[1]
		p2 = each_set[2]
		p3 = each_set[3]
		p1_dic[p1[0]].append([each_set[0],p1])
		p2_dic[p2[0]].append([each_set[0],p2])
		p3_dic[p3[0]].append([each_set[0],p3])
		p123_dic[p1[0]].append([each_set[0],p1])
		p123_dic[p2[0]].append([each_set[0],p2])
		p123_dic[p3[0]].append([each_set[0],p3])

	return [p1_list, p2_list, p3_list, p123_list]