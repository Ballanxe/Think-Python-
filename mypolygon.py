from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
print bob


def square(t,length):
	for i in range(4):
		fd(t,length)
		lt(t)

#square(bob,50)

def polygon_tr():
	

def polygon(t,length,n):
	for i in range(int(360/n)):
		fd(t,length)
		lt(t,n)

#polygon(bob,50,45)

def circle(t,r):
	polygon(t,10,r)

#circle(t=bob,r=10)

def arc(t,lenght,n,angle):
	for i in range(angle/n):
		fd(t,lenght)
		lt(t,n)

#arc(bob,10,10,180)

def circle2(t,r):
	circunference = 2*math.pi*r
	n = int(circunference / 3)+1
	lenght = circunference/n
	polygon(t,n,lenght)

circle2(t=bob,r=50)




wait_for_user()    