__author__ = 'keechow'

# this is a subclass of dictionary
	# from collections import Counter
	#     A = Counter({'a':1, 'b':2, 'c':3})
	#     B = Counter({'b':3, 'c':4, 'd':5})
	#     A + B
    #     Counter({'c': 7, 'b': 5, 'd': 5, 'a': 1})

from file_handler import read4d_result
from file_handler import read5d_result
from file_handler import read6d_result
from separate_by_month import separate_4d
from separate_by_month import separate_5d
from separate_by_month import separate_6d
from num_range_count import count5D_numrange

data_4d = read4d_result("4D.txt")
data_5d = read5d_result("5D.txt")
data_6d = read6d_result("6D.txt")

data_4d_by_month = separate_4d(data_4d)
data_5d_by_month = separate_5d(data_5d)
data_6d_by_month = separate_6d(data_6d)

data_5d_jan = data_5d_by_month[0]

data_5d_jan_count = count5D_numrange(data_5d_jan)


print data_5d_jan_count

print "\n\n\n============== SUCCESSFULLY EXECUTED ================"
print "============== SUCCESSFULLY EXECUTED ================"
print "============== SUCCESSFULLY EXECUTED ================"
