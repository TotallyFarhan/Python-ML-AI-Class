import turtle
import time

screen = turtle.Screen()

class Bullet:
    SPEED = 100

    def __init__(self, owner):
        self.turtle = turtle.Turtle()
        self.turtle.ht()
        self.turtle.speed(0)
        self.turtle.setpos(owner.turtle.pos())
        self.turtle.setheading(owner.turtle.heading())

    def move(self):
        self.turtle.fd(Bullet.SPEED)

    def drawBullet(self):
        t = self.turtle
        startPos = t.pos()
        startHeading = t.heading()
        t.fillcolor("white")
        t.pencolor("white")
        t.begin_fill()
        t.pd()
        t.fd(1)
        t.lt(90)
        t.circle(2)
        t.end_fill()
        
        t.pu()
        t.setpos(startPos)
        t.setheading(startHeading)

class Player:
    MAX_SPEED = 10
    ROTATION_SPEED = 10
    MAX_BULLETS = 5
    
    def __init__(self, color, position, heading):
        self.isAccelerating = False
        self.isTurningLeft = False
        self.isTurningRight = False
        self.speed = 0
        self.color = color
        self.turtle = turtle.Turtle()
        self.turtle.ht()
        self.turtle.speed(0)
        self.turtle.setpos(position)
        self.turtle.setheading(heading)
        self.bullets = list()

    def move(self):
        #Rotate
        if self.isTurningLeft:
            self.turtle.left(Player.ROTATION_SPEED)
        if self.isTurningRight:
            self.turtle.right(Player.ROTATION_SPEED)
        
        #Accelerate
        if self.isAccelerating:
            self.speed += 1
            if self.speed > Player.MAX_SPEED:
                self.speed = Player.MAX_SPEED
            
        else:
            if self.speed > 0:
                self.speed -= 1

        #Move forward
        self.turtle.fd(self.speed)
        

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

    def fire(self):
        self.bullets.append(Bullet(self))

        if len(self.bullets) > Player.MAX_BULLETS:
            self.bullets[0].turtle.clear()
            self.bullets.pop(0)

    def clear(self):
        self.turtle.clear()
        for bullet in self.bullets:
            bullet.turtle.clear()

screen.bgcolor("black")

p1 = Player("blue", (-200, -200), 90)
p2 = Player("red", (200, 200), 270)

#Player 1 Controls
def wPressed():
    p1.isAccelerating = not p1.isAccelerating
def aPressed():
    p1.isTurningLeft = not p1.isTurningLeft
    p1.isTurningRight = False
def dPressed():
    p1.isTurningRight = not p1.isTurningRight
    p1.isTurningLeft = False
def spacePressed():
    p1.fire()
    
def upArrowPressed():
    p2.isAccelerating = not p2.isAccelerating
def leftArrowPressed():
    p2.isTurningLeft = not p2.isTurningLeft
    p2.isTurningRight = False
def rightArrowPressed():
    p2.isTurningRight = not p2.isTurningRight
    p2.isTurningLeft = False
def mouseClicked(x, y):
    p2.fire()


def gameloop():
    p1.clear()
    p2.clear()

    p1.move()
    for bullet in p1.bullets:
        bullet.move()
    
    p2.move()
    for bullet in p2.bullets:
        bullet.move()

    p1.drawShip()
    for bullet in p1.bullets:
        bullet.drawBullet()
    
    p2.drawShip()
    for bullet in p2.bullets:
        bullet.drawBullet()

    turtle.update()
    screen.ontimer(gameloop, 20)

turtle.tracer(0, 0)

screen.onkeypress(wPressed, "w")
screen.onkeypress(aPressed, "a")
screen.onkeypress(dPressed, "d")
screen.onkeypress(spacePressed, "space")

screen.onkeypress(upArrowPressed, "Up")
screen.onkeypress(leftArrowPressed, "Left")
screen.onkeypress(rightArrowPressed, "Right")
screen.onclick(mouseClicked)

screen.listen()

gameloop()
    
