import turtle

draw = turtle.Turtle()
screen = turtle.Screen()

draw.home()

draw.pensize(10)
draw.pencolor('red')

screen.bgcolor('orange')
screen.delay(30)

def f():
    draw.up()
    draw.forward(50)

screen.onkey(f, 'Up')
screen.listen()





turtle.done()
