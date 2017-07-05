def build_url_search_term(start_month, start_year,  num_of_month, company):
	# this method is to generate a list of month&year to be used to generate url search term
	# params: start_date: int, start_year: int, num_of_month: int, company: int,
	# use time.strftime() to get local time in str
	# "%m": month in decimal, "%Y": full year

	# base_url = "http://my.myfreepost.com/en/"
	# search_term = "?dMonth=01&dYear=1996"
	# company_names = "sportstoto", "damacai", "magnum"
	# earliest data for sportstoto = January 1993
	# earliest data for magnum = January 1996
	# earliest data for damacai = January 1997
	# e.g.    http://my.myfreepost.com/en/magnum/4d/top3prize/?dMonth=01&dYear=1998


	### generate a list of month and year wanted to search
	int_start_month = int(start_month)
	int_start_year = int(start_year)
	int_num_of_month = int(num_of_month)


	### determine how many years & months to add based on int_num_of_month
	num_of_year = int_num_of_month / 12
	num_of_mnth = int_num_of_month % 12

	### generate iteration for months between start and end date
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










	company_name = ["", "magnum", "damacai", "sportstoto"]    #list of company's names
	co_name = company_name[company]
	base_url = "http://my.myfreepost.com/en/"
	co_url = co_name + "/4d/top3prize/"





	request_company_name = "\nPlease select company.\n " \
						   "1 = Magnum\n 2 = Damacai\n 3 = SportsToto\n>"

	request_start_month = "\nPlease enter start month. (e.g. 01 or 02)\n>"

	request_start_year = "\nPlease enter start year. (e.g. 2010 or 2012)\n    " \
						 "Earliest year\n    Magnum     = 1996\n    Damacai    = 1997\n    SportsToto = 1993\n>"

	select_end_date_mode = "\nWould you want to specify an end date?\n " \
						   "1 = Yes. Specify month and year\n " \
						   "2 = Specify number of months from start date\n " \
						   "3 = No. Use current month.\n>"    #Strings for requesting user input

	end_date_mode_1_end_month = "\nPlease enter end month\n>"

	end_date_mode_1_end_year = "\nPlease enter end year\n>"

	end_date_mode_2_num_of_month = "\nPlease enter number of months from start month. (Integer only)\n>"



	usr_input_co_name = int(raw_input(request_company_name))
	usr_input_start_month = int( raw_input(request_start_month))
	usr_input_start_year = int(raw_input(request_start_year))
	usr_input_end_date_mode = int(raw_input(select_end_date_mode))

	tuple_start_date = (str(usr_input_start_month),str( usr_input_start_year))
	
	tuple_end_date = ""

	if usr_input_end_date_mode == 3:
		usr_input_end_month = time.strftime("%m")
		usr_input_end_year = time.strftime("%Y")
		tuple_end_date = (usr_input_end_month, usr_input_end_year)

	elif usr_input_end_date_mode == 2:
		usr_input_num_of_month = int(raw_input(end_date_mode_2_num_of_month))
		num_of_year = usr_input_num_of_month / 12  #num of year to add to start year
		num_of_month = usr_input_num_of_month % 12 #num of month to add to start month
		year = usr_input_start_year + num_of_year
		month = usr_input_start_month + num_of_month
		tuple_end_date = (str(month), str(year))
	else:
		usr_input_end_month = raw_input(end_date_mode_1_end_month)
		usr_input_end_year = raw_input(end_date_mode_1_end_year)
		tuple_end_date  =(usr_input_end_month, usr_input_end_year)

	return [tuple_start_date, tuple_end_date, company_name[usr_input_co_name]]


