import turtle
#turtle.shape("food.gif")
#turtle.getshapes()
#turtle.mainloop()


def cool_circle():
	for i in range(360):
		turtle.home()
		turtle.right(i)
		turtle.speed(100000)
		turtle.forward(200)
		turtle.right(45)
		turtle.forward(100)
		turtle.right(90)
		turtle.forward(50)

cool_circle()
turtle.mainloop()