import turtle
import time
import random
from ball import Ball

turtle.tracer(0, 0)
turtle.hideturtle()

RUNNING = True
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

def collide(ball_a, ball_b):
	if ball_a == ball_b:
		return(false)

MY_BALL = Ball(1,2,3,4,50, "pink")
