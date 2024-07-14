import turtle

window = turtle.Screen()
pen = turtle.Turtle()

window.title("Rectangle Creator")

print("This program lets you draw a rectangle!\n")

myColor = input("What color would you like the rectangle to be? ")
pen.color(myColor)

myWidth = int(input("What width would you like the rectangle to have? "))
myHeight = int(input("What height would you like the rectangle to have? "))

pen.fillcolor(myColor)
pen.begin_fill()
pen.fd(myWidth)
pen.rt(90)
pen.fd(myHeight)
pen.rt(90)
pen.fd(myWidth)
pen.rt(90)
pen.fd(myHeight)
pen.rt(90)
pen.end_fill()