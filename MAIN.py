__author__ = 'keechow'

from file_handler import read5d_result

data_5d = read5d_result("5D.txt")

print type(data_5d)
print len(data_5d)