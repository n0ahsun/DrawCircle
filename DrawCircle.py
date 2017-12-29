import turtle
def square(tt):
	for i in range(5):
		tt.forward(80)
		tt.left(90)

def draw():
	a = turtle.Turtle()
	window = turtle.Screen()
	window.bgcolor("yellow")
	a.shape("turtle")
	a.color("red")
	a.speed(3)
	for j in range(20):
		square(a)
		a.left(20)
	window.exitonclick()
draw()