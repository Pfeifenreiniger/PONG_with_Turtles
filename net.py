
from turtle import Turtle

class Net:
    def __init__(self):
        self.body = self.create_net()

    def create_net(self):
        temp_turtles = []
        x_pos = 0
        y_pos = -275
        for i in range(8):
            tim = Turtle()
            tim.hideturtle()
            tim.speed("fastest")
            tim.shape("square")
            tim.color("white")
            tim.turtlesize(stretch_wid=2, stretch_len=0.5)
            tim.penup()
            tim.setx(x_pos)
            tim.sety(y_pos)
            tim.showturtle()
            y_pos += 80
            temp_turtles.append(tim)
        return temp_turtles[:]