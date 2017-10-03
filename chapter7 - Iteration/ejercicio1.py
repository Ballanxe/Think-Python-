import math
a = 4.0  
x = 3.0
y = (x + a / x) / 2

print y

epsilon = 0.01
while True:
	print x
	y = (x + a/x) / 2
	if abs(y-x) < epsilon:
		break
	x = y

def square_root(a,x):
	while True:
		print x
		y = (x + a/x) / 2
		if y == x:
			break
		x = y

def test_square_root(a,x):
	
	while True:
		b = math.sqrt(a)
		print a,
		y = (x + a/x) / 2
		print y,
		print b,
		d = abs(y - x)
		print d
		if a == 9.0:
			break
		a = a + 1.0
		x = y
		
test_square_root(1.0,1.0)

def eval_loop():
	s = "done"
	while True:
		a = raw_input("que desea evaluar?\n")
		f = str(a)
		b = eval(f)
		print b
		if a == s:
			print  d
			break
		d = b



eval_loop()