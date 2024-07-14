import turtle

window = turtle.Screen()
pen = turtle.Turtle()

def circle():
    pen.circle(25)
    
def rectangle():
    pen.forward(50)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
    pen.forward(50)
    
def triangle():
    pen.right(45)
    pen.forward(73)
    pen.right(135)
    pen.forward(100)
    pen.right(135)
    pen.forward(75)
    
shape = input("what shape u want to draw").lower()

if shape == "circle":
    circle()
elif shape == "triangle":
    triangle()
elif shape == "rectangle":
    rectangle()
else:
    print("thats not a shape")
