 __author__ = 'keechow'
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
	run = True
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

	return [tuple_start_date, tuple_end_date, company_name[usr_input_co_name]]

	# return list = [(str_start_month, str_start_year) , (str_end_month, str_end_year), str_co_name]



def url_builder():
	# build a set of URL with different search term to download HTML result
	# generate search term up to latest result

# setting up all the counter to loop month & year for building url
	month_ctr = 01
	sportstoto_yr_ctr = 1993
	magnum_yr_ctr = 1996
	damacai_yr_ctr = 1997

# constructing search url
	url_co = ""
	url_month = ""
	url_year = ""

	search_url = "http://my.myfreepost.com/en/" + url_co + "/4d/top3prize/" +"?dMonth=" + url_month + "&dYear=" + url_year"    #base url for search























