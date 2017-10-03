

def check_fermat(a,b,c,n):
	num1 = a**n + b**n
	num2 = c**n
	if n > 2 and num1 == num2:
		print "Holy Smokes, Fermat was wrong"
	else:
		print "No, that doesnt work"

#check_fermat(2,3,4,n=3)

def numbers():
	a = raw_input("Inserte el primer numero \n")

	b = raw_input("Inserte el segundo numero\n")

	c = raw_input("Inserte el tercer numero\n")
	
	n = raw_input("Inserte el exponente\n")

	check_fermat(int(a),int(b),int(c),int(n))

#numbers()


def is_triangle(a,b,c):
	int(a)
	int(b)
	int(c)
	if a + b < c or a + c < b or b + c < a:
		print "NO"
	else:
		print "YES"


#is_triangle(5,3,2)

def def_triangle():
	inserte = "Inserte un lado \n"
	a = raw_input(inserte)
	b = raw_input(inserte)
	c = raw_input(inserte)
	is_triangle(int(a),int(b),int(c))

def_triangle()


