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
		self.pu()
		self.x = x
		self.y = y
		self.goto(x,y)

	def check_bor(self):
		if self.xcor() > 150:
			self.hideturtle()
			print("You cant see your ball")

		if self.xcor() < -150:
			self.hideturtle()
			print("You cant see your ball")

		if self.ycor() > 150 :
			self.hideturtle()
			print("You cant see your ball")

		if self.ycor() < -150 :
			self.hideturtle()
			print("You cant see your ball")


	



def check_collision(ball1, ball2):
	r1 = ball1.radius
	r2 = ball2.radius
	x1 = ball1.xcor()
	x2 = ball2.xcor()
	y1 = ball1.ycor()
	y2 = ball2.ycor()

	d = pow((x2-x1),2)+ pow((y2-y1),2)
	d = sqrt(d)
	rad =r1 + r2
	if rad >= d:
		print("my name is jeff")

	if r1 > r2:
		Xx = random.randrange(-150, 150)
		Yy = random.randrange(-150, 150)
		ball2.goto(Xx,Yy)

	if r2 > r1:
		Xx = random.randrange(-150, 150)
		Yy = random.randrange(-150, 150)
		ball1.goto(Xx,Yy)



#the pink ball should disapear but it doesnt

ball1 = Ball(250,100,12,"pink", 1)
ball2 = Ball(230,100,20, "orange", 2)

#ball1.goto(250,100)
#ball2.goto(-250,-100)

check_collision(ball1, ball2)
















mainloop()