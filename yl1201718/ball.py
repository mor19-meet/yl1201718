from turtle import *
import turtle

class Ball(Turtle):
	def __init__(self, x, y, dx, dy, r, color):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r

		self.color(color)
		self.pu()
		self.goto(x,y)
		self.shape("circle")
		self.shapesize(r/10)

	def move (self, screen_width, screen_height):
		self.screen_width = screen_width
		self.screen_height = screen_height

		current_x = self.x
		new_x = current_x + self.dx

		current_y = self.y
		new_y = current_y + self.dy

		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		top_side_ball = new_y + self.r
		bottom_side_ball = new_y - self.r

		turtle.goto(new_x,new_y)

		if new_x >= screen_width:
			self.dx = self.dx - 20

		if new_x >= screen_width:
			self.dx = self.dx + 20

		if new_y >= screen_height:
			self.dy = self.dy - 20

		if new_y >= screen_height:
			self.dy = self.dy + 20

