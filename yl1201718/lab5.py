from turtle import *
import turtle
import random
colormode(255)

#exercise 1
#class Square(Turtle):
#	def __init__(self,size):
#		Turtle.__init__(self)
#		self.shapesize(size)
#		self.shape("square")

#	def random_color(self):
#		r = random.randint(0,255)
#		g = random.randint(0,255)
#		b = random.randint(0,255)
#		self.color((r,g,b))
	

#square1= Square(2)
#square1.random_color()

#extra hard
class rectangle(Turtle):
	def __init__(self,shape,width, hight):
	
		#self.width = width
		#self.hight = hight
		Turtle.__init__(self)
		register_shape("rect", ((0,0), (width,0), (width,hight), (0,hight)))
		self.shape("rect")
	
	def random_color(self):
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color((r,g,b))



rect1 = rectangle(1,100,100)
rect1.random_color()

mainloop()























#exercise 2
class Hexagon (Turtle):
	def __init__(self,hex):
		Turtle.__init__(self)
		turtle.home()
		turtle.begin_poly()
		turtle.forward(70)
		turtle.left(60)
		turtle.forward(70)
		turtle.left(60)
		turtle.forward(70)
		turtle.left(60)
		turtle.forward(70)
		turtle.left(60)
		turtle.forward(70)
		turtle.left(60)
		turtle.forward(70)
		turtle.left(60)
		turtle.end_poly()
		self.hex = turtle.get_poly()

	#def random_color(self):
	#	r = random.randint(0,255)
	#	g = random.randint(0,255)
	#	b = random.randint(0,255)
	#	self.color((r,g,b))
		
hex1 = Hexagon(5)


mainloop()