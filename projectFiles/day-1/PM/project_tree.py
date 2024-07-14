import turtle
 
window = turtle.Screen()
pen = turtle.Turtle()

window.title("Tree")

#Trunk
pen.color("brown")
pen.fillcolor("brown")
pen.begin_fill()
pen.forward(50)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(200)
pen.end_fill()

#Leaves
pen.right(90)
pen.forward(25)
pen.color("green")
pen.fillcolor("green")
pen.begin_fill()
pen.circle(100)
pen.left(90)
pen.forward(20)
pen.right(180)
pen.circle(60)
pen.right(180)
pen.circle(60)
pen.end_fill()
