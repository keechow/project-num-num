from file_handler import read
import num_analysis as na

result = read("4D.txt")
latest_result = read("4D-latest.txt")

latest_3prize = []    #latest prize 1,2,3
for each_draw in latest_result:
    latest_3prize.append(each_draw[2])
    latest_3prize.append(each_draw[3])
    latest_3prize.append(each_draw[4])

all_4D_num = na.gen_num()    #all 4D num, 0000 - 9999
i1_num = na.get_list_4()    #all 4 digits are the same
i4_num = na.get_list_3()  #3 digits are the same
i1_num2 = na.get_list_4()

prize1 = []
prize2 = []
prize3 = []

for each_draw in result:
	year = each_draw[0][-2:]
	p1 = each_draw[2]
	p2 = each_draw[3]
	p3 = each_draw[4]
	if year == "14" or year == "15" or year == "16":
		prize1.append(p1)
		prize2.append(p2)
		prize3.append(p3)
prize123 = prize1 + prize2 + prize3

# we want to eliminate same element within prize123
prize123_clean = na.clean_duplicate(prize123)
eliminated_num_list = na.clean_duplicate(i1_num + i4_num + prize123_clean) #nums that we don't want

clean_4d_num_list = []
for each in all_4D_num:
	if each not in eliminated_num_list:
		clean_4d_num_list.append(each)

print "prize123_clean len: ", len(prize123_clean)
print "i1num len: ", len(i1_num)
print "i4num len: ", len(i4_num)
print "clean 4d: ", len(clean_4d_num_list)
print "el list: ", len(eliminated_num_list)




