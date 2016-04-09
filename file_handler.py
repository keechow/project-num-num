"""
Name: file_handler.py
Objective: write and read from file
Params: list of strings
Author: The Echo Telion Project <echo.telion@gmail.com>

"""
import time

def write_to(list_input):
    file_name = raw_input("Please enter file name\n")

    if len(file_name) == 0:
        sys_time = time.strftime("%c")        #get sys time in format:- 
        ys_time = sys_time.replace("/","")        #09/05/15 16:51:05
        s_time = ys_time.replace(":","")        #strip away all unwanted char
        _time = s_time.replace(" ","_")      #now:- 090515_165105 => use as filename
        file_name = _time + ".txt"
    else:
        file_name += ".txt"
    
    txt_file = open(file_name, "w")
    for each_line in list_input:
        txt_file.write(each_line)
        txt_file.write("\n")
    
    txt_file.close()
    
    
def read5d_result(file_name):
    # read str data from 5D result file
    # return a list with element type<list>
    # return list element: [draw date, 1st prize, 2nd prize, 3rd prize]

    return_list = []
    txt_file = open(file_name, "r")
    data = txt_file.read()
    s_data= data.split("\n")
            #split data at \n and return as list
    for each in s_data:
        each_s_data = each[7:-1]    #we don't want draw no. and the last string \r
        return_list.append(each_s_data.split(","))
    return return_list

def read6d_result(file_name):
    # read str data from 5D result file
    # return a list with element type<list>
    # return list element: [draw date, 1st prize]

    return_list = []
    txt_file = open(file_name, "r")
    data = txt_file.read()
    s_data = data.split("\n")
            #split data at \n and return as list
    for each in s_data:
        each_strip = each[7:-1]    #we don't want draw no. and the last string \r
        return_list.append(each_strip.split(","))

    return return_list

def read4d_result(file_name):
    # read str data from 4D result file
    # return a list with element type<list>
    # return list element: [draw num, 1st, 2nd, 3rd, 10 special prize, 10 conso prize]

    return_list = []
    txt_file = open(file_name, "r")
    data = txt_file.read()
    s_data = data.split("\n")
        #split data at \n and return as list
    for each in s_data:


#Below are codes for testing purposes

data = read6d_result("6D.txt")

print data[:10]
print "========== end =========="





    
