# importing the turtle library
import turtle as tp

#score
playerA=0
playerB=0

# creating the playing screen
window=tp.Screen()
window.title("Ping-Pong Game")
window.bgcolor("black")
window.setup(width=800,height=600)
window.tracer(0)

# creating leftpad
leftpad=tp.Turtle()
leftpad.speed(0)
leftpad.shape("square")
leftpad.color("white")
leftpad.shapesize(stretch_wid=5,stretch_len=1)
leftpad.penup()
leftpad.goto(-350,0)

# creating rightpad
rightpad=tp.Turtle()
rightpad.speed(0)
rightpad.shape("square")
rightpad.color("white")
rightpad.shapesize(stretch_wid=5,stretch_len=1)
rightpad.penup()
rightpad.goto(350,0)

# creating ball
ball=tp.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdir=0.2
ballydir=0.2

# creating pt for updating scorecard
pt=tp.Turtle()
pt.speed(0)
pt.color("Blue")
pt.penup()
pt.hideturtle()
pt.goto(0,260)
pt.write("score",align="center",font=('Arial',24,'normal'))

# moving the left and right pad by using def function
def leftpaddleup():
    y=leftpad.ycor()
    y=y+90
    leftpad.sety(y)
def leftpaddledown():
    y=leftpad.ycor()
    y=y-90
    leftpad.sety(y)
def rightpaddleup():
    y=rightpad.ycor()
    y=y+90
    rightpad.sety(y)
def rightpaddledown():
    y=rightpad.ycor()
    y=y-90
    rightpad.sety(y)

# assigning keys to play the game
window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')

while True:
    # moving the ball
    window.update()
    ball.setx(ball.xcor()+ballxdir)
    ball.sety(ball.ycor()+ballydir)
    
    # setting up border
    if ball.ycor()>290:
        ball.sety(290)
        ballydir=ballydir*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ballydir=ballydir*-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdir=ballxdir
        playerA=playerA+1
        pt.clear()
        pt.write("Player A:{}                    Player B:{}".format(playerA,playerB),align='center',font=('Arial',24,'normal'))
    if ball.xcor()<-390: 
        ball.goto(0,0)
        ballxdir=ballxdir* -1
        playerB=playerB+1
        pt.clear()
        pt.write("Player A: {}                   Player B: {} ".format(playerA,playerB),align="center",font=('Arial',24,"normal"))
    
    # handling the collisions
    if(ball.xcor()>340) and (ball.xcor()<350) and (ball.ycor()<rightpad.ycor() + 40 and ball.ycor()>rightpad.ycor() - 40):
        ball.setx(340)
        ballxdir=ballxdir*-1

    if(ball.xcor()<-340) and (ball.xcor()>-350) and (ball.ycor()<leftpad.ycor() + 40 and ball.ycor()>leftpad.ycor() - 40):
        ball.setx(-340)
        ballxdir=ballxdir*-1