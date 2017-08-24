from  get_result_frm_webpage import build_url_search_term
from  get_result_frm_webpage import parse_data_from_url

import num_analysis

import json


str_data_collection_start_month = "01"
str_data_collection_start_year = "2016"
str_data_collection_num_of_month = "19"
str_data_collection_company = "damacai"

list_search_url = build_url_search_term(str_data_collection_start_month, str_data_collection_start_year, str_data_collection_num_of_month, str_data_collection_company)
		## containing a list of URL to be used to request data from Internet

list_data_whole_range = []
		## list for containing all parsed data

for each_month_data_url in list_search_url:
	monthly_data = parse_data_from_url(each_month_data_url)
	for each_draw_data in monthly_data:
		list_data_whole_range.append(each_draw_data)

## save list_data_whole_range into JSON file for future use
def save_to_file(data):
	with open("data_file.txt","w") as outputfile:
		json.dump(data, outputfile)

def load_from_file():
	return_list_data = []
	with open("data_file.txt") as inputfile:
		json_load_from_file = json.load(inputfile)
		for each_draw in json_load_from_file:
			str_data = [s.encode('utf-8') for s in each_draw]
			return_list_data.append(str_data)
	return return_list_data


