"""
Name: separate_num_module.py
Objective: Take combined result list and separate nums into respective categories, i-24, i12, i6, i4
Params: Result List
Return: List with 4 elements, i-24, i-12, i6, i4
Author: The Echo Telion Project <echo.telion@gmail.com>

"""
import num_analysis

def separate_num(combined_result):
    list_num1 = num_analysis.get_list_1()         #standard generated num with no repeating digits
    list_num2 = num_analysis.get_list_2()         #standard generated num with 2 repeating digits
    list_num3 = num_analysis.get_list_3()         #standard generated num with 3 repeating digits 
    list_num4 = num_analysis.get_list_4()         #standard generated num with 4 repeating digits
    list_num_double = num_analysis.get_list_double()    #standard generated num with double double repeating digits

    list_result_num1 = []        #list storing 1 digit num from result
    list_result_num2 = []        #list storing 2 digit num from result
    list_result_num3 = []        #list storing 3 digit num from result
    list_result_num4 = []        #list storing 4 digit num from result
    list_result_num_double = []        #list storing double double digit num from result

    for each in combined_result:
        if each[0] in list_num4:
            list_result_num4.append(each)
        elif each[0] in list_num3:
            list_result_num3.append(each)
        elif each[0] in list_num_double:
            list_result_num_double.append(each)
        elif each[0] in list_num2:
            list_result_num2.append(each)
        else:
            list_result_num1.append(each)

    return_list = []
    return_list.append(list_result_num1)
    return_list.append(list_result_num2)
    return_list.append(list_result_num_double)
    return_list.append(list_result_num3)
    return_list.append(list_result_num4)

    return return_list
"""
#Below are codes for testing
from parsing_module import get_data
from combine_module import combine

combined_result = combine(get_data())

num_cat_sorted_result = separate_num(combined_result)
##print "Combined result:" , len(combined_result)
##print "i24: ", len(num_cat_sorted_result[0])
##print "i12: ", len(num_cat_sorted_result[1])
##print "i6: ", len(num_cat_sorted_result[2])
##print "i4: ", len(num_cat_sorted_result[3])
##print "i1: ", len(num_cat_sorted_result[4])
##print "Total ", (len(num_cat_sorted_result[0]) + len(num_cat_sorted_result[1]) + len(num_cat_sorted_result[2]) + len(num_cat_sorted_result[3])+ len(num_cat_sorted_result[4]))

for each in num_cat_sorted_result[2]:
    print each

print


print "**********     END OF EXECUTION     **********"
"""    
    
