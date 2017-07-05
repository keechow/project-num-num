int_num_of_month = 36
int_start_month = 1
int_start_year = 2000

list_year = []
list_month = []

while int_num_of_month > 0:
	while int_start_month <13 and int_num_of_month >= 0:
		list_month.append(str(int_start_month))
		list_year.append(str(int_start_year))
		int_start_month = int_start_month + 1
		int_num_of_month -=1
	int_start_year += 1
	int_start_month = 1

print(list_month)
print(list_year)

