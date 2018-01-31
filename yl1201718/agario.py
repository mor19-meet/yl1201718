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
	while dx == 0:
		dx = random.randint(- MINIMUM_BALL_DX , MAXIMUM_BALL_DX)

	while dy == 0:
		dy = random.randint(- MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	

	random_ball = Ball(x,y,dx,dy,radius,color)

	BALLS.append(random_ball)


#part 1: move all balls
def move_all_balls():
	for mor in BALLS:
		mor.move(SCREEN_WIDTH , SCREEN_HEIGHT)

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
				radius_a = ball_a.r 
				radius_b = ball_b.r

				r = random.randint(0,255)
				g = random.randint(0,255)
				b = random.randint(0,255)

				X_coordinate = random.randint(- SCREEN_WIDTH + random_ball.r , SCREEN_WIDTH - random_ball.r ) 
				Y_coordinate = random.randint( - SCREEN_HEIGHT + random_ball.r , SCREEN_HEIGHT - random_ball.r)
				radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
				color = (r,g,b)
				X_axis_speed = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				Y_axis_speed = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

				while X_axis_speed == 0:
					X_axis_speed = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)

				while Y_axis_speed == 0:
					Y_axis_speed = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

				if radius_a > radius_b:
					ball_b.x = X_coordinate
					ball_b.y = Y_coordinate
					ball_b.dx = X_axis_speed
					ball_b.dy = Y_axis_speed
					ball_b.r = radius
					ball_b.color = color
					ball_b.shapesize = (ball_b.r / 10)
					ball_a.r = ball_a.r + 1

				else:
					ball_a.x = X_coordinate
					ball_a.y = Y_coordinate
					ball_a.dx = X_axis_speed
					ball_a.dy = Y_axis_speed
					ball_a.r = radius
					ball_a.color = color
					ball_a.shapesize = (ball_b.r / 10)
					ball_b.r = ball_b.r + 1


#part 4 : check collision with my ball
def check_myball_collision():
	global MY_BALL
	for random_ball in BALLS:
		if collide(random_ball ,MY_BALL):
			radius_random_ball = random_ball.r
			radius_MY_BALL = MY_BALL.r

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
	X_coordinate = event.x - SCREEN_WIDTH
	Y_coordinate = SCREEN_HEIGHT - event.y

	MY_BALL.goto(X_coordinate , Y_coordinate)


#part 5.1 : move it!:
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

#part 6 : the while loop:
while RUNNING == True:
	if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2:
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2

	if SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2:
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

	move_all_balls()
	check_all_balls_collision()
	check_myball_collision()

	if check_myball_collision == False:
		RUNNING = False

	turtle.getscreen().update()
	time.sleep(1/60)



	



	


				

		


	




























turtle.mainloop()