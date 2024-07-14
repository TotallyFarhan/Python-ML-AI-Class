import turtle
 
screen = turtle.Screen()
pen = turtle.Turtle()

screen.title("Shape Selector")

def drawSquare(size):
    pen.fd(size)
    pen.rt(90)
    pen.fd(size)
    pen.rt(90)
    pen.fd(size)
    pen.rt(90)
    pen.fd(size)
    pen.rt(90)

def drawTriangle(size):
    pen.lt(60)
    pen.fd(size)
    pen.rt(120)
    pen.fd(size)
    pen.rt(120)
    pen.fd(size)
    pen.rt(180)

pen.ht()

while True:
    print("I can draw a circle, square, or triangle")
    choice = input("Enter the shape you want: ").lower()
    pen.clear()
    
    if choice == "circle":
        pen.circle(100)
    elif choice == "square":
        drawSquare(100)
    elif choice == "triangle":
        drawTriangle(100)
    elif choice == "quit":
        break
    else:
        print("\nSorry. I do not know how to draw that yet.\n")

screen.bye()
print("Goodbye!")

