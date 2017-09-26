
"""
File name:  get_result_frm_webpage.py
Objective: Get raw draw result data from webpage
Note:

"""

# parse from website
# base_url = "http://my.myfreepost.com/en/"
# search_term = "?dMonth=01&dYear=1996"
# company_names = "sportstoto", "damacai", "magnum"
# earliest data for sportstoto = January 1993
# earliest data for magnum = January 1996
# earliest data for damacai = January 1997
# e.g.    http://my.myfreepost.com/en/magnum/4d/top3prize/?dMonth=01&dYear=1998
# we want to create a URL builder, to loop months and year, something like URI Builder


#### IMPORT THIS ####  IMPORT THAT ####
from bs4 import BeautifulSoup
import urllib2
import time
#### IMPORT THIS ####  IMPORT THAT ####

def request_user_input():
	# this method is to display messages asking for user input to
	# determine start date and end date of data wanted
	# use time.strftime() to get local time in str
	# "%m": month in decimal, "%Y": full year
	# list_return_data = [(str_start_month, str_start_year) , (str_end_month, str_end_year), str_co_name)

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

	company_name = ["", "magnum", "damacai", "sportstoto"]    #list of company's names

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

		# return list = [(str_start_month, str_start_year) , (str_end_month, str_end_year), str_co_name]
	return [tuple_start_date, tuple_end_date, company_name[usr_input_co_name]]

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

	### we have a list of month and a list of year.
	### we want to extract each element from each list to build a complete url

	return_list_complete_query_url = []
	element_counter = 0
	base_url = "http://my.myfreepost.com/en/"
	search_term_month = "/4d/top3prize/?dMonth="
	search_term_year = "&dYear="

	while (element_counter < int(num_of_month)):
# e.g.    http://my.myfreepost.com/en/magnum/4d/top3prize/?dMonth=01&dYear=1998
		search_url = base_url + company + search_term_month + list_month[element_counter]+search_term_year+list_year[element_counter]
		return_list_complete_query_url.append(search_url)
		element_counter += 1

	return return_list_complete_query_url

## Next is to open url and parse the data

def parse_data_from_url(str_url):
	## params: string url
	## objective: parse data from url
	## return a list containing [draw_date, p1_nu,, p2_num, p3_num]
    ## [['19990331', '8498', '3773', '6576'], ..., ['19990302', '1996', '0472', '2328']]

	soup = BeautifulSoup(urllib2.urlopen(str_url),"lxml")    #get raw data from URL
	unicode_soup_txt = soup.tr.get_text()
	str_soup_txt = unicode_soup_txt.encode('utf-8')    #raw data in unicode, encode into string

	## there are a lot of unwanted string in raw data, slice to get draw date, p1, p2, p3
	index_of_Draw_DateTop_3_prizes = str_soup_txt.index("Draw DateTop 3 prizes")
	str_soup_txt_slice_front = index_of_Draw_DateTop_3_prizes
	str_soup_txt_slice_end = -170

	sliced_str_soup_txt = str_soup_txt[str_soup_txt_slice_front:str_soup_txt_slice_end]
	list_sliced_str_soup_txt =[]
	for each in sliced_str_soup_txt.splitlines():
		if not len(each) == 0:
			each_date = each[:4]+each[5:7]+each[8:10]
			each_p1 = each[10:14]
			each_p2 = each[17:21]
			each_p3 = each[24:]
			list_element = [each_date, each_p1, each_p2, each_p3]
			list_sliced_str_soup_txt.append(list_element)
	return (list(reversed(list_sliced_str_soup_txt)))[:-1]


####################
##      TESTING GROUND     ##
####################


