from turtle import *
import random
import math
#colornode(255)

class Ball(Turtle):
	def __init__(self,x,y,radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
		self.x = x
		self.y = y

	

ball1 = Ball(100,100,12,"pink", 12)
ball2 = Ball(0,0,20, "orange", 6)


def check_collision(ball1, ball2):
	r1 = ball1.radius
	r2 = ball2.radius
	x1 = ball1.xcor()
	x2 = ball1.xcor()
	y1 = ball1.ycor()
	y2 = ball1.ycor()

	d = pow((x2-x1),2)+ pow((y2-y1),2)
	d = sqrt(d)
	rad =r1 + r2
	if rad >= d:
		print("my name is jeff")




check_collision(ball1, ball2)













mainloop()