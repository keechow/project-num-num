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

def url_builder():
	# build a set of URL with different search term to download HTML result
	# generate search term up to latest result
	# using time.strftime() to get local time in str
	# %m: month in decimal, %Y: full year

    current_month = time.strftime("%m") #Jan = 01, Oct = 10
	current_year = time.strftime("%Y") #1996, 2017, 1998

# setting up all the counter to loop month & year for building url
	month_ctr = 01
	sportstoto_yr_ctr = 1993
	magnum_yr_ctr = 1996
	damacai_yr_ctr = 1997

# constructing search url
	url_co = ""
	url_month = ""
	url_year = ""

	search_url = "http://my.myfreepost.com/en/" + url_co + "/4d/top3prize/" +"?dMonth=" + url_month + "&dYear=" + url_year"









