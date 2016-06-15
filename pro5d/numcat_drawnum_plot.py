import matplotlib.pyplot as plt

from file_handler import read5d_result_w_draw_no as read5d

x_elements = []
y_elements=[]

data = read5d("5D.txt")

for each_set in data[-30:]:
	prize1 = each_set[2]
	prize1_numcat = int(prize1[0])
	y_elements.append(prize1_numcat)
	x_elements.append(int(each_set[0]))

print x_elements

plt.plot(x_elements,y_elements, "rs")
plt.show()
