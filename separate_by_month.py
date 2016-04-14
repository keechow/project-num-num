"""
Name: separate_by_month.py
Author: echo.telion@gmail.com
Objective: Separate result data into 12 list according to month
Input: List of result, sorted by date
Output: List of result, separated into each month

"""

def separate_by_month(data):
	jan = []
	feb = []
	mar = []
	apr = []
	may = []
	jun = []
	jul = []
	aug = []
	sep = []
	octo = []
	nov = []
	dec = []

	month_dict = {"01":jan, "02":feb, "03":mar, "04":apr, "05":may, "06":jun, "07":jul,
				  "08":aug, "09":sep, "10":octo, "11":nov, "12":dec}

		# we will use dic, key-value pair to match each result's month and append the result into 			respective month list

	for each_data in data:
			data_month = each_data[0][4:6]
			month = month_dict.get(data_month)
			month.append(each_data)

	return [jan,feb,mar,apr,may,jun,jul,aug,sep,octo,nov,dec]
