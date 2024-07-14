import turtle
import time

screen = turtle.Screen()

class Bullet:
    SPEED = 100

    def __init__(self, owner):
        self.owner = owner
        self.turtle = turtle.Turtle()
        self.turtle.ht()
        self.turtle.speed(0)
        self.turtle.setpos(owner.turtle.pos())
        self.turtle.setheading(owner.turtle.heading())

    def move(self):
        steps = 20 
        stepSpeed = Bullet.SPEED / steps

        if self.owner == p1: enemy = p2
        else: enemy = p1

        for i in range(steps):
            self.turtle.fd(stepSpeed)

            if self.hittest(enemy):
                enemy.isAlive = False

    def hittest(self, other):
        return self.turtle.distance(other.turtle) < 20  

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
        self.isAlive = True
        self.health = 10
        self.isMoving = False
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

        if self.turtle.xcor() >= 350:
            self.turtle.setx(-350)
        elif self.turtle.xcor() <= -350:
            self.turtle.setx(350)

        if self.turtle.ycor() >= 350:
            self.turtle.sety(-350)
        elif self.turtle.ycor() <= -350:
            self.turtle.sety(350)
        

    def drawShip(self):
        if not self.isAlive: return
        
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

        if self.isMoving:
            t.fillcolor("orange")
            t.begin_fill()
            t.pu()
            t.rt(90)
            t.bk(30)
            t.circle(6)
            t.end_fill()
            t.pu()
            t.rt(90)
            t.fd(2)
            t.rt(90)
            t.begin_fill()
            t.pd()
            t.circle(6.5)
            t.end_fill()
            t.pu()
            

        # RESET TURTLE
        t.pu()
        t.setpos(startPos)
        t.setheading(startHeading)

    def fire(self):
        if not self.isAlive: return
        
        self.bullets.append(Bullet(self))

        if len(self.bullets) > Player.MAX_BULLETS:
            self.bullets[0].turtle.clear()
            self.bullets.pop(0)

    def clear(self):
        self.turtle.clear()
        for bullet in self.bullets:
            bullet.turtle.clear()

screen.bgcolor("black")

p1 = Player("blue", (200, -200), 90)
p2 = Player("red", (200, 200), 270)

#Player 1 Controls
def wPressed():
    p1.isAccelerating = not p1.isAccelerating
    p1.isMoving = not p1.isMoving
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
    p2.isMoving = not p2.isMoving
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

turtle.done()
