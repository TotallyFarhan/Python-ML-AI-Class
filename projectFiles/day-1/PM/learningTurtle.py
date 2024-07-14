import turtle
 
window = turtle.Screen()
pen = turtle.Turtle()

window.title("Shapes")

diameter = 300

pen.pensize(10)
pen.color("blue")

pen.up()
pen.backward(diameter/2)
pen.left(90)
pen.forward(diameter/2)
pen.right(90)

pen.down()
pen.forward(diameter)
pen.right(90)
pen.forward(diameter)
pen.right(90)
pen.forward(diameter)
pen.right(90)
pen.forward(diameter)
pen.left(90)
pen.backward(diameter/2)

pen.color("red")
pen.circle(diameter/2)
