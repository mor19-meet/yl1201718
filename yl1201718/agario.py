from turtle import *
import turtle
import time
import random
from ball import Ball
import math
turtle.bgcolor("black")
turtle.colormode(255)

turtle.tracer(0)
turtle.hideturtle()
turtle.pu()

RUNNING = True
SLEEP = 0.0077

SCREEN_WIDTH = int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()/2)

#part 0: creating the balls
MY_BALL = Ball(1,2,3,4,20, "pink")
MY_BALL.goto(10,10)

NUMBER_OF_BALLS = 6

MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 40

MINIMUM_BALL_DX = -1
MAXIMUM_BALL_DX = 1

MINIMUM_BALL_DY = -1
MAXIMUM_BALL_DY = 1

BALLS = []

for i in range (NUMBER_OF_BALLS):
	x = random.randint(- SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y = random.randint(- SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	r = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
	color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

	new_ball = Ball(x,y,dx,dy,r,color)
	BALLS.append(new_ball)


#part 1: move all balls
def move_all_balls():
	for ball in BALLS:
		ball.move(SCREEN_WIDTH , SCREEN_HEIGHT)

#part 2: check for a ball collisions

def collide(ball_a , ball_b):
	if ball_a == ball_b:
		return False

	d = (math.pow(ball_b.xcor() - ball_a.xcor() , 2)) + (math.pow(ball_b.ycor() - ball_a.ycor(), 2))
	d = math.sqrt(d)

	if ((d) <= (ball_a.r + ball_b.r)):
		return True
	else:
		return False

#part 3:check collision for all balls
def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a , ball_b) == True:

				print("all collided")
				ball_a_radius = ball_a.r
				ball_b_radius = ball_b.r

				if ball_a_radius > ball_b_radius:
					ball_a.r += 1
				else:
					ball_b.r += 1

				X_coordinate = random.randint(- SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				Y_coordinate = random.randint(- SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)


				X_axis_speed = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				Y_axis_speed = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

				while (X_axis_speed == 0 and Y_axis_speed == 0):
					X_axis_speed = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
					Y_axis_speed = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

				radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
				color = (random.randint(0,255), random.randint(0,255) , random.randint(0,255))

				if ball_a.r > ball_b.r:
					ball_b.goto(X_coordinate , Y_coordinate)
					ball_b.dx = X_axis_speed
					ball_b.dy = Y_axis_speed
					ball_b.r = radius
					ball_b.color(color)
					ball_b.shapesize(ball_b.r/10)

					ball_a.r = ball_a.r + 1
					ball_a.shapesize(ball_a.r / 10)
				

				else:
					ball_a.goto(X_coordinate , Y_coordinate)
					ball_a.dx = X_axis_speed
					ball_a.dy = Y_axis_speed
					ball_a.r = radius
					ball_a.color(color)
					ball_a.shapesize(ball_a.r/10)

					ball_b.shapesize(ball_b.r/10)
					ball_b.r = ball_b.r + 1
score = 0
#part 4 : check collision with my ball
def check_myball_collision():
	for new_ball in BALLS:
		if collide(MY_BALL , new_ball) == True:

			print("my collide")

			r_new_ball= new_ball.r
			r_MY_BALL = MY_BALL.r
			if MY_BALL.r < new_ball.r:
				turtle.clear()
				turtle.goto(0,0)
				turtle.color("white")
				turtle.write("you lost!", move=False, align="center", font=("Arial", 40, "normal"))
				time.sleep(2)
				quit()
				return False

			X_coordinate = random.randint(- SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			Y_coordinate = random.randint(- SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)

			X_axis_speed = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
			Y_axis_speed =  random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

			while X_axis_speed == 0 and Y_axis_speed == 0:
				X_axis_speed = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				Y_axis_speed = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)

			radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
			color = color = (random.randint(0,255), random.randint(0,255) , random.randint(0,255))

			new_ball.r = radius
			new_ball.goto(X_coordinate , Y_coordinate)
			new_ball.dx = X_axis_speed
			new_ball.dy = Y_axis_speed
			new_ball.color(color)
			new_ball.shapesize(new_ball.r/10)

			MY_BALL.r = MY_BALL.r + 1
			MY_BALL.shapesize(MY_BALL.r / 10)

			global score
			score = score + 1
			print (score)
			turtle.goto(-SCREEN_WIDTH + 30, SCREEN_HEIGHT-30)
			turtle.color("white")
			turtle.clear()
			turtle.write("score: " + str(score), move=False, align="left", font=("Arial", 16, "normal"))
			
	return True


#part 5: movearound

def movearound(event):
	X_mouse = event.x - SCREEN_WIDTH
	Y_mouse = SCREEN_HEIGHT - event.y

	MY_BALL.goto(X_mouse , Y_mouse)


#part 5.1 : move it!:
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

#part 6 : the while loop:
while RUNNING == True:
	if (SCREEN_WIDTH != int(getcanvas().winfo_width()/2) or SCREEN_HEIGHT != int(getcanvas().winfo_height()/2)):
		SCREEN_WIDTH = int(getcanvas().winfo_width()/2)
		SCREEN_HEIGHT = int(getcanvas().winfo_height()/2)

		# MY_BALL.move(SCREEN_HEIGHT , SCREEN_WIDTH)

	move_all_balls()
	check_all_balls_collision()
	RUNNING = check_myball_collision()
	
	turtle.getscreen().update()
	time.sleep(1/60)


hideturtle()




