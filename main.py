from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import ScoreBoard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.title('Pong Game')

screen.listen()
screen.tracer(0)
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = ScoreBoard()

screen.onkey(r_paddle.r_up, 'Up')
screen.onkey(r_paddle.r_down, 'Down')
screen.onkey(l_paddle.r_up, 'w')
screen.onkey(l_paddle.r_down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

    if score.r_score == 5:
        game_is_on = False
        score.game_end('Player B')

    elif score.l_score == 5:
        game_is_on = False
        score.game_end('Player A')

screen.exitonclick()
