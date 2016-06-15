"""
Name: num_cat_sort_module.py

Objective: Produce a list of num for specified number category

Params: combined_result_list, num_cat

Method: num_cat_sort()
        - produce a list of num for specified num cat
        result_separator()
        - produce a list with all result separated by num cat
        
Return: list containing numbers for num_cat
Author: The Echo Telion Project <echo.telion@gmail.com>

"""
import num_analysis as na

def num_cat_sorter(num_list, num_cat):
    all_list = []
        #list containing all separated result. special for result_separator
    list_i24 = []
    list_i12 = []
    list_i6 = []
    list_i4 = []
    list_i1 = []

    for each in num_list:
        oc = na.calc_occurence(each[0])
        if oc == 2:
            if na.check_double_double(each[0]):
                list_i6.append(each)
            else:
                list_i12.append(each)
        elif oc == 4:
            list_i1.append(each)
        elif oc == 3:
            list_i4.append(each)
        else:
            list_i24.append(each)

    if num_cat == 1:
        return list_i24
    elif num_cat == 2:
        return list_i12
    elif num_cat == 3:
        return list_i4
    elif num_cat == 4:
        return list_i1
    elif num_cat == 9999:
        all_list.append(list_i24)
        all_list.append(list_i12)
        all_list.append(list_i6)
        all_list.append(list_i4)
        all_list.append(list_i1)
        return all_list        
    else:
        return list_i6

def get_all_result(result):
    return num_cat_sorter(result, 9999)

def get_i24(result):
    return num_cat_sorter(result, 1)

def get_i12(result):
    return num_cat_sorter(result, 2)

def get_i6(result):
    return num_cat_sorter(result, 5)

def get_i4(result):
    return num_cat_sorter(result, 3)

def get_i1(result):
    return num_cat_sorter(result, 4)

    


