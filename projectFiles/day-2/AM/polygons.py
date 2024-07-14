import turtle
 
screen = turtle.Screen()
turtle = turtle.Turtle()
 
screen.title("User Input")
 
num_sides = int(input("How many sides on your regular polygon? "))
side_length = 400 / num_sides
angle = 360 / num_sides

turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(0, num_sides):
    turtle.forward(side_length)
    turtle.right(angle)
turtle.end_fill()

