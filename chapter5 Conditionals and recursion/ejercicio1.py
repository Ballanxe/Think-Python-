def do_n(f,n=1):
	if n<=0:
		return
	f()
	do_n(f,n-1)

def hablar():
	print "hola"


do_n(hablar,5)


def check_fermat(a,b,c,n):
	if n > 2 and (a**n+b**n==c**n):
		print "Holy Smokes, Fermat was wrong"
	else:
		print "No, that doesnt work"

check_fermat(2,3,4,n=3)


