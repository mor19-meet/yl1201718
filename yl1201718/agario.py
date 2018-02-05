from turtle import *
import turtle
import time
import random
from ball import Ball
import math
turtle.colormode(255)


turtle.tracer(0)
turtle.hideturtle()
turtle.pu()

RUNNING = True
SLEEP = 0.0077


SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

#part 0: creating the balls
MY_BALL = Ball(1,2,3,4,50, "pink")


NUMBER_OF_BALLS = 5

MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100



MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5

MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

BALLS = []

for i in range (NUMBER_OF_BALLS):
	x = random.randint(- SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(- SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
	color = (random.random(), random.random(), random.random())

#make sure dy and dx are never 0:
	# while dx == 0:
	# 	dx = random.randint(- MINIMUM_BALL_DX , MAXIMUM_BALL_DX)

	# while dy == 0:
	# 	dy = random.randint(- MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	

	random_ball = Ball(x,y,dx,dy,radius,color)

	BALLS.append(random_ball)


#part 1: move all balls
def move_all_balls():
	for ball in BALLS:
		ball.move(SCREEN_WIDTH , SCREEN_HEIGHT)

#part 2: check for a ball collisions

def collide(ball1 , ball_b):
	if ball1 == ball_b:
		return False

	d = (math.pow(ball_b.x - ball1.x , 2)) + (math.pow(ball_b.y - ball1.y , 2))
	d = math.sqrt(d)

	if (d + 10) <= (ball1.r + ball_b.r):
		return True

	else:
		return False
		

#part 3:check collision for all balls
def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a , ball_b):

				radius_a = ball_a.r 
				radius_b = ball_b.r

				X_coordinate = random.randint(- SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS) 
				Y_coordinate = random.randint( - SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
				color = color = (random.randint(0,255), random.randint(0,255) , random.randint(0,255))
				X_axis_speed = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				Y_axis_speed = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

				while X_axis_speed == 0:
					X_axis_speed = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)

				while Y_axis_speed == 0:
					Y_axis_speed = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

				if ball_a.r > ball_b.r:
					ball_b.goto(X_coordinate , Y_coordinate)
					ball_b.x = X_coordinate
					ball_b.y = Y_coordinate
					ball_b.dx = X_axis_speed
					ball_b.dy = Y_axis_speed
					ball_b.r = radius
					ball_b.color = "color"

					ball_a.shapesize = (ball_a.r / 10)
					ball_a.r = ball_a.r + 1

				else:
					ball_b.goto(X_coordinate , Y_coordinate)
					ball_a.x = X_coordinate
					ball_a.y = Y_coordinate
					ball_a.dx = X_axis_speed
					ball_a.dy = Y_axis_speed
					ball_a.r = radius
					ball_a.color = "color"

					ball_b.shapesize = (ball_b.r / 10)
					ball_b.r = ball_b.r + 1


#part 4 : check collision with my ball
def check_myball_collision():
	for random_ball in BALLS:
		if collide(random_ball ,MY_BALL):
			# radius_random_ball = random_ball.r
			# radius_MY_BALL = MY_BALL.r

			if random_ball.r > MY_BALL.r:
				return False

			# 	MY_BALL.goto(X_coordinate , Y_coordinate)
			# 	MY_BALL.x = X_coordinate
			# 	MY_BALL.y = Y_coordinate
			# 	MY_BALL.dx = X_axis_speed
			# 	MY_BALL.dy = Y_axis_speed
			# 	MY_BALL.r = radius
			# 	MY_BALL.color = color
			# 	MY_BALL.shapesize = (ball_b.r / 10)
			# 	random_ball.r = ball_a.r + 1

			if MY_BALL.r > random_ball.r:

				X_coordinate = random.randint(- SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS) 
				Y_coordinate = random.randint( - SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
				color = (random.randint(0,255), random.randint(0,255) , random.randint(0,255))
				X_axis_speed = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				Y_axis_speed = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

				while X_axis_speed == 0:
					X_axis_speed = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)

				while Y_axis_speed == 0:
					Y_axis_speed = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)


				random_ball.goto(X_coordinate , Y_coordinate)
				random_ball.x = X_coordinate
				random_ball.y = Y_coordinate
				random_ball.dx = X_axis_speed
				random_ball.dy = Y_axis_speed
				random_ball.r = radius
				random_ball.color = "color"

				MY_BALL.shapesize = (MY_BALL.r / 10)
				MY_BALL.r = ball1.r + 1

	return(True)


#part 5: movearound

def movearound(event):
	X_mouse = event.x - SCREEN_WIDTH
	Y_mouse = SCREEN_HEIGHT - event.y

	MY_BALL.goto(X_mouse , Y_mouse)


#part 5.1 : move it!:
turtle.Screen().getcanvas().bind("<Motion>", movearound)
turtle.getscreen().listen()

#part 6 : the while loop:
while RUNNING == True:
	if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2 or SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2:
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

	move_all_balls()
	check_all_balls_collision()
	
	MY_BALL.move(SCREEN_WIDTH , SCREEN_HEIGHT)
	RUNNING = check_myball_collision()
		

	turtle.getscreen().update()
	time.sleep(1/60)



	



	


				

		


	




























turtle.mainloop()