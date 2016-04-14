__author__ = 'keechow'

from file_handler import read5d_result
from separate_by_month import separate_by_month

data_5d = read5d_result("5D.txt")
result_by_month = separate_by_month(data_5d)

jan = result_by_month[0]
print len(jan)
print jan


print "\n\n\n============== SUCCESSFULLY EXECUTED ================"
print "============== SUCCESSFULLY EXECUTED ================"
print "============== SUCCESSFULLY EXECUTED ================"