import calendar

#calendar.weekday(year, month, day)

print (calendar.weekday(2017,10,2))
list_wed_draw = []
list_sat_draw = []
list_sun_draw = []
list_other_draw = []

dict_draw_day_list = {2:list_wed_draw, 5:list_sat_draw, 7:list_sun_draw}

dict_draw_day_list[2].append("hahaha")


if 2 in dict_draw_day_list:
    print dict_draw_day_list[2]