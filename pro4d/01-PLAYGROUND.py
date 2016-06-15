# 1) need file handler to read results from data file

from file_handler import read
import num_analysis as na

data = read("4D.txt")
print len(data)

print na.gen_num()