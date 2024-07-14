import turtle

screen = turtle.Screen()

class Player:
    def __init__(self, color):
        self.color = color
        self.turtle = turtle.Turtle()
        self.turtle.ht()
        self.turtle.speed(0)

    def drawShip(self):
        t = self.turtle
        startPos = t.pos()
        startHeading = t.heading()

        # DRAW BODY
        t.fillcolor(self.color)
        t.pencolor(self.color);
        t.begin_fill()
        t.pu()
        t.fd(15)
        t.pd()
        t.rt(30 + 120)
        t.fd(40)
        t.rt(120)
        t.fd(40)
        t.rt(120)
        t.fd(40)
        t.end_fill()

        # RESET TURTLE
        t.pu()
        t.setpos(startPos)
        t.setheading(startHeading)
        
        # DRAW COCKPIT
        t.fillcolor("black")
        t.pencolor("black");
        t.begin_fill()
        t.pu()
        t.fd(3)
        t.lt(90)
        t.pd()
        t.circle(6)
        t.end_fill()

        # RESET TURTLE
        t.pu()
        t.setpos(startPos)
        t.setheading(startHeading)


screen.bgcolor("black")

p1 = Player("blue")

t.ht()
t.speed(0)
drawShip("blue")



    
    
