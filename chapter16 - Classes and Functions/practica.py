class Time(object):

	hour = 11
	minute = 59
	second = 30

def print_time():
	time = Time()
	print time.hour,':',time.minute,':',time.second
	print '%.2d:%.2d:%.2d', % (time.hour, time.minute, time.second)


print_time()