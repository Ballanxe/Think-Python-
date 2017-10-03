
def compare(x,y):
	if x > y:
		return 1
	elif x == y:
		return 0
	elif x < y:
		return -1

compare(4,3)


def is_between(x,y,z):
    return x <= y and y <= z

is_between(2,5,8)