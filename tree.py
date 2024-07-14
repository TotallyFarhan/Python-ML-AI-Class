import turtle

window = turtle.Screen()
pen = turtle.Turtle()

window.title("Drawing Graphics")

pen.fillcolor("brown")
pen.begin_fill()

pen.color("brown")

pen.up()

pen.backward(100)

pen.down()

pen.forward(200)
pen.right(90)
pen.forward(300)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(300)


pen.end_fill()

pen.fillcolor("green")
pen.begin_fill()

pen.color("green")

pen.circle(100)

pen.end_fill()

pen.up()

pen.forward(135)
pen.right(90)
pen.forward(235)
pen.left(90)

pen.down()

pen.fillcolor("green")
pen.begin_fill()

pen.color("green")

pen.circle(140)

pen.end_fill()

pen.up()

pen.backward(225)
pen.right(90)
pen.forward(63)

pen.down()

pen.fillcolor("green")
pen.begin_fill()

pen.color("green")

pen.circle(100)

pen.end_fill()



