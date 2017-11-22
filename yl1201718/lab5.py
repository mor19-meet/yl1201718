from turtle import *
import turtle
import random
colormode(255)

class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")
		
	def random_color(self):
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color((r,g,b))
	

square1= Square(2)
square1.random_color()

mainloop()