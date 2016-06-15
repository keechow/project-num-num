"""
Name: gen_i12.py
Objectives: generate a list of i12_num for a particular double digit
Params: None
Return: list of i12 num
Author: The Echo Telion Project <echo.telion@gmail.com>

"""
result = []
def generate_num():
    global result
    dd_list = ["00","11","22","33","44","55","66","77","88","99"]
    lst_2d = range(100)     #this is for the remaining 2digit to be attached to double digit

    str_lst_2d = []
    for each in lst_2d:
        el = str(each)
        if len(el) < 2:
            el = "0" + el        
        if el[0] != el[1]:        #both remainder 2D cannot be the same
            if int(el[1]) < int(el[0]):
                el = el[1]+el[0]
            str_lst_2d.append(el)  
    final_lst = []
    for each in str_lst_2d:        #remove repeating digit such as 0012 and 0021
        if not each in final_lst:
            final_lst.append(each)
    
    for each in dd_list:        #attach remainder 2D to header DD
        each_dd_list = []
        for num in final_lst:
            if not each[0] in num:    #remainder 2D can't be the same as DD
                new = each+num
                each_dd_list.append(new)        #separate each list of result according to DD
        result.append(each_dd_list)

def get_i12_00():
    generate_num()
    return result[0]

def get_i12_11():
    generate_num()
    return result[1]

def get_i12_22():
    generate_num()
    return result[2]

def get_i12_33():
    generate_num()
    return result[3]

def get_i12_44():
    generate_num()
    return result[4]

def get_i12_55():
    generate_num()    
    return result[5]

def get_i12_66():
    generate_num()
    return result[6]

def get_i12_77():
    generate_num()
    return result[7]

def get_i12_88():
    generate_num()
    return result[8]

def get_i12_99():
    generate_num()
    return result[9]
