__author__ = 'keechow'

minute = 0
hour = 0
num_of_cycle = 100

while num_of_cycle > 0:
	while minute < 60 and num_of_cycle >= 0:
		print("Hour: " + str(hour) +" Min: " + str(minute))
		print(num_of_cycle)
		minute += 1
		num_of_cycle -=1
	hour += 1
	minute = 0

