__author__ = 'keechow'

from file_handler import read4d_result
from file_handler import read5d_result
from file_handler import read6d_result
from separate_by_month import separate_4d
from separate_by_month import separate_5d
from separate_by_month import separate_6d

data_4d = read4d_result("4D.txt")
data_5d = read5d_result("5D.txt")
data_6d = read6d_result("6D.txt")

data_4d_by_month = separate_4d(data_4d)
data_5d_by_month = separate_5d(data_5d)
data_6d_by_month = separate_6d(data_6d)

#print result6d_by_month[0]

print "\n\n\n============== SUCCESSFULLY EXECUTED ================"
print "============== SUCCESSFULLY EXECUTED ================"
print "============== SUCCESSFULLY EXECUTED ================"