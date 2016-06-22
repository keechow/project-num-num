from file_handler import read
import num_analysis as na

all_num = na.gen_num()
result = read("4D.txt")
latest_result = read("4D-latest.txt")

# generate 3 list for 1st prize, 2nd prize, 3rd prize numbers drawn for 2013, 2014, 2015, 2016

prize1 = []
prize2 = []
prize3 = []

for each_draw in result:
	year = each_draw[0][-2:]
	p1 = each_draw[2]
	p2 = each_draw[3]
	p3 = each_draw[4]
	if year == "16" or year == "15" or year == "14" or year == "13" or year == "12" or year == "11" or year == "10" or year == "09" or year == "08" or year == "07":
		prize1.append(p1)
		prize2.append(p2)
		prize3.append(p3)

print len(prize1)
print len(prize2)
print len(prize3)

latest_3prize = []
for each_draw in latest_result:
    latest_3prize.append(each_draw[2])
    latest_3prize.append(each_draw[3])
    latest_3prize.append(each_draw[4])

match1 = set(prize1) & set(latest_3prize)
match2 = set(prize2) & set(latest_3prize)
match3 = set(prize3) & set(latest_3prize)

print len(match1)
print
print match1
print
print match2
print
print match3