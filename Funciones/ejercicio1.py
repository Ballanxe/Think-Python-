
#primera forma de hacerlo
#
#
#

def techo():
	print "+ - - - - + - - - - +"


def columnas():
	print "|         |         |"

def do_twice(c):
	c()
	c()


def techo_y_columnas():
	techo()
	do_twice(columnas)

techo_y_columnas()

def grid():
	do_twice(techo_y_columnas)
	techo()

print "next"

grid()

def techo(c,d):
	c()
	d()

#Segunda forma no termine :(

def roof():
	print "+",
	print "- - +"

def wall():
	print "!     !"

def nRoof():
	print "  - -"
	print "+"

def nWall():
	print "      !"


def do_three(f):
	f()
	f()
	f()

def xWall():
	roof()
	do_three(wall)

def xxWall():
	do_twice(xWall)

def xxxWall():
	xxWall()
	roof()

def nRoofnWall():
	nRoof()
	do_three(nWall)

def nr2():
	do_twice(nRoofnWall)

def grid():
	return nr2(), xxxWall()

def nothing():
	print "        "

def kdkd(w,f):
	print str(w)+str(f)


kdkd(xxxWall,nr2)






