import turtle
import time
import random
from ball import Ball
import math
colormode(255


turtle.tracer(0, 0)
turtle.hideturtle()

RUNNING = True
SLEEP = 0.0077

SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

def collide(ball_a, ball_b):
	if ball_a == ball_b:
		return(false)

#part 0: creating the balls
MY_BALL = Ball(1,2,3,4,50, "pink")

NUMBER_OF_BALLS = 5

MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 10


#make sure dy and dx are never 0!!!
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5

MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

for i in range (NUMBER_OF_BALLS):
	x = random.randint(- SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(- SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(- MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	dy = random.randint(- MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	radius = random.randint(- MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())

while dx == 0:
	dx = random.randint(- MINIMUM_BALL_DX , MAXIMUM_BALL_DX)

while dy == 0:
	dy = random.randint(- MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	

random_ball = Ball(x,y,dx,dy,radius,color)

BALLS.append(random_ball)


#part 1: move all balls
def move_all_balls():
	for ball in BALLS:
		random_ball.move(SCREEN_WIDTH , SCREEN_HEIGHT)

#part 2: check for a ball collisions

def collide(ball_a , ball_b):
	if ball_a == ball_b:
		return (False)

	d = (math.pow(ball_b.x - ball_a.x , 2)) + (math.pow(ball_b.y - ball_a.y , 2))
	d = math.sqrt(d)

	if (d + 10) <= (ball_a.r + ball_b.r):
		return (True)

	else:
		return(False)
		

#part 3:check collision for all balls
def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a , ball_b):
				radius_a = ball_a.radius 
				radius_b = ball_b.radius

				r = random.randint(0,255)
				g = random.randint(0,255)
				b = random.randint(0,255)

				X_coordinate = random.randint() 
				Y_coordinate = random.randint()
				radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
				color = (r,g,b)
				X_axis_speed = random.randint()
				Y_axis_speed = random.randint()

				while X_axis_speed == 0:
					X_axis_speed = random.randint()

				while Y_axis_speed == 0:
					Y_axis_speed = random.randint()

				if radius_a > radius_b:
					ball_b = Ball(X_coordinate , Y_coordinate , X_axis_speed , Y_axis_speed , radius , color)
					ball_b.shapesize = (ball_b.r / 10)
					ball_a.r = ball_a.r + 1

				else:
					ball_a = Ball(X_coordinate , Y_coordinate , X_axis_speed , Y_axis_speed , radius , color)
					ball_a.shapesize = (ball_b.r / 10)
					ball_b.r = ball_b.r + 1


#part 4 : check collision with my ball
def check_myball_collision():
	for random_ball in BALLS:
		if collide(random_ball , MY_BALL):
			radius_random_ball = random_ball.radius 
			radius_MY_BALL = MY_BALL.radius

			if radius_random_ball > radius_MY_BALL:
				return(False)

				MY_BALL = Ball(X_coordinate , Y_coordinate , X_axis_speed , Y_axis_speed , radius , color)
				MY_BALL.shapesize = (ball_b.r / 10)
				random_ball.r = ball_a.r + 1

			if radius_random_ball < radius_MY_BALL:
				random_ball = Ball(X_coordinate , Y_coordinate , X_axis_speed , Y_axis_speed , radius , color)
				random_ball.shapesize = (ball_b.r / 10)
				MY_BALL.r = ball_a.r + 1

	return(True)


#part 5: movearound

def movearound(event):
	X_coordinate(event.x - SCREEN_WIDTH)
	Y_coordinate(SCREEN_HEIGHT - event.y)

	MY_BALL.goto(X_coordinate , Y_coordinate)


#part 5.1 : move it!

turtle.getcanvas().bind("<Motion>", movearound)
listen()


#part 6 : the while loop


	


				

		


	




























turtle.mainloop()