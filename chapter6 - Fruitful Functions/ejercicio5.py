def is_power(a,b):
	d = a/b
	return a % b == 0 or d % b == 0

print is_power(10,2)