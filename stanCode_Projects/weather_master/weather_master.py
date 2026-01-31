"""
File: weather_master.py
Name:Roger141
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100  # Exit value.

def main():
	"""
	Collects temperature inputs until the user enters EXIT,then displays the highest, lowest, average temperature,
	and the count of cold days (below 16 degrees).
	"""
	print('staneCode \"Weather Master 4.0\"!')
	n = int(input('Next Temperature: (or -100 to quiz)?'))
	if n == EXIT:
		print('No temperatures were entered.')
		return
	total = n
	count = 1
	highest = n
	lowest = n
	cold_days = 0
	if n < 16:
		cold_days += 1
	while True:
		n = int(input('Next Temperature: (or -100 to quiz)?'))
		if n == EXIT:
			break
		total += n
		count += 1
		if n > highest:
			highest = n
		if n < lowest:
			lowest = n
		if n < 16:
			cold_days += 1
	avg = total / count
	print('Highest temperature =' + str(highest))
	print('Lowest temperature =' + str(lowest))
	print('Average =' + str(avg))
	print(str(cold_days) + 'cold day(s)')






# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
