import turtle
window = turtle.Screen()
window.title ("square")
window.bgcolor("yellow")

board = turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.right(90)

turtle.done()