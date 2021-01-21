import turtle;
import os

wn = turtle.Screen()

wn.title("Pong by Kamil")
wn.bgcolor("pink")
wn.setup(width=800,height=600)
wn.tracer(0)

# Scores
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.color('black') #color
paddle_a.speed(0) #not the move speed
paddle_a.shape('square') # shape
paddle_a.penup() # not ot draw a line when it moves
paddle_a.goto(-350,0) #initial position
paddle_a.shapesize(stretch_wid=5,stretch_len=1) #make it a rectangle
# Paddle B

paddle_b = turtle.Turtle()
paddle_b.color("black")
paddle_b.shape("square")
paddle_b.speed(0)
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)


# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color("#242424")
ball.goto(0,0)
ball.penup()
ball.dx = 0.7
ball.dy = 0.7


# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {}  Player B: {} ".format(score_a,score_b),align="center",font=('Courier',24,"normal"))


# game functions

def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y)
    

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)

# KeyBindings

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


# Main Game Loop
while True:
    #TK_SILENCE_DEPRECATION=1
    wn.update() 

    # Ball movement
    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor()+ball.dx)

    # Border Checking
        #top border
    if ball.ycor() > 290:
        #ball.sety(290)
        ball.dy *= -1
        os.system("afplay ./bounce.wav&")

        #bottom border
    if ball.ycor() < -290:
        #ball.sety(-290)
        ball.dy *= -1
        os.system("afplay ./bounce.wav&")
        
        #right border
    if ball.xcor() > 390:
        os.system("afplay ./bounce.wav&")
        ball.goto(0,0)
        ball.dx *= -1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(score_a,score_b),align="center",font=('Courier',24,"normal"))

        #left borderw
    if ball.xcor() < -390:
        os.system("afplay ./bounce.wav&")
        ball.goto(0,0)
        ball.dx *= -1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(score_a,score_b),align="center",font=('Courier',24,"normal"))


    # Ball and Paddle collision

    if((ball.xcor() > 340 and ball.xcor()< 345) and (ball.ycor()>paddle_b.ycor()-50 and ball.ycor()<paddle_b.ycor()+50)):
        ball.dx *= -1
        os.system("afplay ./bounce.wav&")
    
    if((ball.xcor() < -340 and ball.xcor()>-345) and (ball.ycor()>paddle_a.ycor()-50 and ball.ycor()<paddle_a.ycor()+50)):
        ball.dx *= -1
        os.system("afplay ./bounce.wav&")
        