import turtle
import time
import random
from ball import Ball

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
MAXIMUM_BALL_RADIUS = 100


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


random_ball = Ball(x,y,dx,dy,radius,"pink")

BALLS.append(random_ball)


#part 1: move all balls
def move_all_balls():
	for ball in BALLS:
		random_ball.move(SCREEN_WIDTH , SCREEN_HEIGHT)

#part 2: check for a ball collisions

def collide(ball_a , ball_b):
	if ball_a == ball_b:
		return (False)

	d = (pow(ball_b.x - ball_a.x)) + (pow(ball_b.y - ball_a.y))
	d = sqrt(d)

	if (d + 10) <= (ball_a.r + ball_b.r):
		return (True)

	else:
		return(False)
		

#part 3:check collision for all balls
def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if ball_a == ball_b:
				#there is a line missing!
				ball_a_radius = r
				ball_b_radius = r

X coordinate = random.randint()



























turtle.mainloop()