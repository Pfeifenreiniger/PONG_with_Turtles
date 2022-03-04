"""
A PONG clone made with the aid of the Python turtle library.
The game is part of my #100DaysOfCode challenge (day 22)
Code by Kevin Spathmann (Pfeifenreiniger on GitHub: https://github.com/Pfeifenreiniger)
"""

from turtle import Turtle, Screen
from paddle import Paddle
from net import Net
from ball import Ball
import time, random

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG™ With Turtles")
screen.tracer(0)

score_turtle = Turtle()
score_turtle.penup()
score_turtle.color("white")
score_turtle.hideturtle()
score_turtle.goto(0, 240)

paddle_l = Paddle("l")
paddle_r = Paddle("r")
net = Net()
ball = Ball()


def player_input():
    screen.onkeypress(key="Up", fun=paddle_l.move_up)
    screen.onkeypress(key="Down", fun=paddle_l.move_down)

def cpu_input():
    if random.randint(0,5) > 0:
        if ball.body.ycor() > paddle_r.body[0].ycor():
            paddle_r.move_up()
        elif ball.body.ycor() < paddle_r.body[-1].ycor():
            paddle_r.move_down()
    else:
        random_cpu_behavior = random.randint(0, 3)
        if random_cpu_behavior == 0:
            paddle_r.move_up()
        elif random_cpu_behavior == 1:
            paddle_r.move_down()
        else:
            pass

def score_display():
    score_turtle.clear()
    score_turtle.write(str(paddle_l.score) + "      " + str(paddle_r.score), move=False, align="center", font=("comic sans MS", 34, "normal"))

running = True
screen.listen()
while running:
    player_input()
    cpu_input()
    ball.move()
    screen.update()
    time.sleep(0.1)

    for i in paddle_l.body:
        if ball.body.distance(i) <= 20:
            ball.hit_by_paddle_l = True
    for j in paddle_r.body:
        if ball.body.distance(j) <= 20:
            ball.hit_by_paddle_r = True

    if ball.lost_for_paddle_l:
        paddle_r.score += 1
        ball.lost_for_paddle_l = False
        ball.body.color("red")
        paddle_l.reset_pos("l")
        paddle_r.reset_pos("r")
        ball = Ball()
    if ball.lost_for_paddle_r:
        paddle_l.score += 1
        ball.lost_for_paddle_r = False
        ball.body.color("red")
        paddle_l.reset_pos("l")
        paddle_r.reset_pos("r")
        ball = Ball()

    score_display()

screen.exitonclick()