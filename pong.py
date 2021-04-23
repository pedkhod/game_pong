import turtle



wn = turtle.Screen()
wn.title('pong by ped')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)
#valuable
score_a=0
score_b=0

#paddle a

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)
#paddle b

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
#ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.25
ball.dy = 0.25

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0,260)
pen.write('player A: 0 player B: 0', align='center',font=("arial",20, 'normal'))


# function
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
#function for paddle b
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)
#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")










#maim function
while True:
    wn.update()


    #movie ball
    ball.setx(ball.xcor()  + ball.dx)
    ball.sety(ball.ycor()+ ball.dy)
    #top and bottom
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() <- 290 :
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor()>410 :
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write('player A: {} player B: {}'.format(score_a,score_b), align='center',font=("arial",20, 'normal'))

    if ball.xcor() <-410 :
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write('player A: {} player B: {} '.format(score_a ,score_b ), align='center',font=("arial",20, 'normal'))

    #paddel and ball collision
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()< paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50 ):
        ball.setx(340)
        ball.dx*=-1        
        
    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()< paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50 ):
       ball.setx(- 340)
       ball.dx*=-1
