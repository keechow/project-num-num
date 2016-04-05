from parsing_module import print_each
from parsing_module4 import get_data
from port2excel import port_num
from combine_module import str_combine
from combine_module import combine
import num_cat_sort_module
    #get_i24, get_i12, get_i6, get_i4, get_i1
    #get_all_result : [[i24],[i12],[i6],[i4],[i1]]
from sorting_module import sort
        # sort(combined_result, prize_cat)
        # 0 = number,    1 = Total,      2 = Top3
        # 3 = 1st Prize, 4 = 2nd Prize,  5 = 3rd Prize
        # 6 = Starter,   7 = Consolation

from date_simulator import date_creator

from file_handler import write_to
        # str_combine() has to be used to produce string data suitable for saving into txt file

from i12_analysis import separate
from i12_analysis import identify
        

## ===== WEB PARSING STAGE ===== ##

print "result_24m : 2013/09/01 to 2013/09/30\n"
result_24m_raw = get_data("2013/09/01", "2013/09/30")

print "result_23m : 2013/10/01 to 2013/10/31\n"
result_23m_raw = get_data("2013/10/01", "2013/10/31")

print "result_22m : 2013/11/01 to 2013/11/30\n"
result_22m_raw = get_data("2013/11/01", "2013/11/30")

print "result_21m : 2013/12/01 to 2013/12/31\n"
result_21m_raw = get_data("2013/12/01", "2013/12/31")

print "result_20m : 2014/01/01 to 2014/01/31\n"
result_20m_raw = get_data("2014/01/01", "2014/01/31")

print "result_19m : 2014/02/01 to 2014/02/28\n"
result_19m_raw = get_data("2014/02/01", "2014/02/28")

print "result_18m : 2014/03/01 to 2014/03/31\n"
result_18m_raw = get_data("2014/03/01", "2014/03/31")

print "result_17m : 2014/04/01 to 2014/04/30\n"
result_17m_raw = get_data("2014/04/01", "2014/04/30")

print "result_16m : 2014/05/01 to 2014/05/31\n"
result_16m_raw = get_data("2014/05/01", "2014/05/31")

print "result_15m : 2014/06/01 to 2014/06/30\n"
result_15m_raw = get_data("2014/06/01", "2014/06/30")

print "result_14m : 2014/07/01 to 2014/07/31\n"
result_14m_raw = get_data("2014/07/01", "2014/07/31")

print "result_13m : 2014/08/01 to 2014/08/31\n"
result_13m_raw = get_data("2014/08/01", "2014/08/31")

print "result_12m : 2014/09/01 to 2014/09/30\n"
result_12m_raw = get_data("2014/09/01", "2014/09/30")

print "result_11m : 2014/10/01 to 2014/10/31\n"
result_11m_raw = get_data("2014/10/01", "2014/10/31")

print "result_10m : 2014/11/01 to 2014/11/30\n"
result_10m_raw = get_data("2014/11/01", "2014/11/30")

print "result_9m : 2014/12/01 to 2014/12/31\n"
result_9m_raw = get_data("2014/12/01", "2014/12/31")

print "result_8m : 2015/01/01 to 2015/01/31\n"
result_8m_raw = get_data("2015/01/01", "2015/01/31")

print "result_7m : 2015/02/01 to 2015/02/28\n"
result_7m_raw = get_data("2015/02/01", "2015/02/28")

print "result_6m : 2015/03/01 to 2015/03/31\n"
result_6m_raw = get_data("2015/03/01", "2015/03/31")

print "result_5m : 2015/04/01 to 2015/04/30\n"
result_5m_raw = get_data("2015/04/01", "2015/04/30")

print "result_4m : 2015/05/01 to 2015/05/31\n"
result_4m_raw = get_data("2015/05/01", "2015/05/31")

print "result_3m : 2015/06/01 to 2015/06/30\n"
result_3m_raw = get_data("2015/06/01", "2015/06/30")

print "result_2m : 2015/07/01 to 2015/07/31\n"
result_2m_raw = get_data("2015/07/01", "2015/07/31")

print "result_1m : 2015/08/01 to 2015/08/31\n"
result_1m_raw = get_data("2015/08/01", "2015/08/31")

result_raw = [result_24m_raw,result_23m_raw,result_22m_raw,result_21m_raw,result_20m_raw,
              result_19m_raw,result_18m_raw,result_17m_raw,result_16m_raw,result_15m_raw,
              result_14m_raw,result_13m_raw,result_12m_raw,result_11m_raw,result_10m_raw,
              result_9m_raw,result_8m_raw,result_7m_raw,result_6m_raw,result_5m_raw,
              result_4m_raw,result_3m_raw,result_2m_raw,result_1m_raw]


## ===== Number Analysis ===== ##
result_combined = []
for each in result_raw:
    new = combine(each)
    result_combined.append(new)

     # just take i12 num
i12 = []
for each in result_combined:
    new = num_cat_sort_module.get_i12(each)
    i12.append(new)

    # sort to get TOP3 prize
i12_TOP3 = []
for each in i12:
    new = sort(each, 2)
    i12_TOP3.append(new)

    # separate top 50 of TOP3 into list according to each double digit
i12_TOP3_top50_separated = []
for each in i12_TOP3:
    new = separate(each[:50])
    i12_TOP3_top50_separated.append(new)

    # append each double digit count into a list for easy display
i12_TOP3_top50_digit_count = []
for each in i12_TOP3_top50_separated:
    digit_count = []
    for one in each:
        digit_count.append(len(one))
    i12_TOP3_top50_digit_count.append(digit_count)

    # identify the prevalent single digit paired with each double digit
    # i12_TOP3_top50_separated = list containing 24 element type<list>
    #        each element is i12_TOP3_top50 for the month --> list with 10 elements --> 00,11,...,99
    #        each list contains combined result parsed from web page --> ["4D num",total,top3,1st,2nd,3rd,spe,conso]
### 24m_i12_TOP3_top50_separated = i12_TOP3_top50_separated[0]
### 24m_i12_TOP3_top50_00 = 24m_i12_TOP3_top50[0]
### 24m_i12_TOP3_top50_00_single = identify(24m_i12_TOP30_top50_00)

i12_TOP3_top50_separated_identified = []
for each_month in i12_TOP3_top50_separated:
    monthly_i12_TOP3_top50_dd = []
    for each_dd in each_month:
        #monthly_i12_TOP3_top50_dd_sd = []
        sd = identify(each_dd)
        #monthly_i12_TOP3_top50_dd_sd.append(sd)
        monthly_i12_TOP3_top50_dd.append(sd)    
    i12_TOP3_top50_separated_identified.append(monthly_i12_TOP3_top50_dd)

    
    # we only want to focus on double digit 00, 22, 55, 33
    # i12_TOP3_top50_sort_single[month][double_digit][result]
i12_TOP3_top50_sep_iden_00 = []
for each_month in i12_TOP3_top50_separated_identified:
    monthly = []
    for each_d in each_month[0]:
        monthly.append(len(each_d))
    i12_TOP3_top50_sep_iden_00.append(monthly)

i12_TOP3_top50_sep_iden_22 = []
for each_month in i12_TOP3_top50_separated_identified:
    monthly = []
    for each_d in each_month[2]:
        monthly.append(len(each_d))
    i12_TOP3_top50_sep_iden_22.append(monthly)

i12_TOP3_top50_sep_iden_55 = []
for each_month in i12_TOP3_top50_separated_identified:
    monthly = []
    for each_d in each_month[5]:
        monthly.append(len(each_d))
    i12_TOP3_top50_sep_iden_55.append(monthly)

i12_TOP3_top50_sep_iden_33 = []
for each_month in i12_TOP3_top50_separated_identified:
    monthly = []
    for each_d in each_month[3]:
        monthly.append(len(each_d))
    i12_TOP3_top50_sep_iden_33.append(monthly)

## ===== PRINT OUT RESULT ===== ##

print "\nResult for 00\n"
counter = 24
for each in i12_TOP3_top50_sep_iden_00:
    print counter
    print each
    print
    counter -= 1

print "\nResult for 22\n"
counter = 24
for each in i12_TOP3_top50_sep_iden_22:
    print counter
    print each
    print
    counter -= 1

print "\nResult for 55\n"
counter = 24
for each in i12_TOP3_top50_sep_iden_55:
    print counter
    print each
    print
    counter -= 1

print "\nResult for 33\n"
counter = 24
for each in i12_TOP3_top50_sep_iden_33:
    print counter
    print each
    print
    counter -= 1




print "========== END OF EXECUTION =========="
"""
## ===== SAVE DATA TO TXT FILE ==== ##

result_24m_combined_str = str_combine(result_24m_raw)
result_12m_combined_str = str_combine(result_12m_raw)
result_6m_combined_str = str_combine(result_6m_raw)
result_3m_combined_str = str_combine(result_3m_raw)
result_1m_combined_str = str_combine(result_1m_raw)

write_to(result_24m_combined_str)
write_to(result_12m_combined_str)
write_to(result_6m_combined_str)
write_to(result_3m_combined_str)
write_to(result_1m_combined_str)
"""

print "========== END OF EXECUTION =========="



#Below are Testing codes
"""

raw_result = get_data()
        # Get result list based on date range entered

combined_result = combine(raw_result)
        # Combine number and occurrences into same element

print "1 digit: ", len(list_result_num1)
print
print "2 digit: ", len(list_result_num2)
print
print "3 digit: ", len(list_result_num3)
print
print "4 digit: ", len(list_result_num4)
print
print "double digit: ", len(list_result_num_double)
print
print "Result len: ", len(combined_result)
print

#Pass draw dates
sep15 = [1]
aug15 = [1,2,4,5,8,9,12,15,16,19,22,23,26,29,30]
jul15 = [1,4,5,8,11,12,15,18,19,22,25,26,29]
jun15 = [2,3,6,7,10,13,14,17,20,21,24,27,28]
may15 = [2,3,5,6,9,10,13,16,17,20,23,24,26,27,30,31]
apr15 = [1,4,5,7,8,11,12,15,18,19,22,25,26,28,29]
mar15 = [1,3,4,7,8,11,14,15,18,21,22,25,28,29,31]
feb15 = [1,3,4,7,8,11,14,15,17,18,21,22,24,25,28]
jan15 = [3,4,6,7,10,11,14,17,18,21,24,25,27,28,31]
"""
