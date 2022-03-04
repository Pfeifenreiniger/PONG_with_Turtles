
from turtle import Turtle

class Paddle:
    def __init__(self, side):
        self.body = self.create_body(side)
        self.score = 0
        self.move_pace = 15

    def create_body(self, side):
        temp_turtles = []
        for i in range(5):
            tim = Turtle()
            tim.hideturtle()
            tim.speed("fastest")
            tim.shape("square")
            tim.color("white")
            tim.penup()
            temp_turtles.append(tim)
        if side == "r":
            return self.start_pos(temp_turtles, "r")
        else:
            return self.start_pos(temp_turtles, "l")

    def start_pos(self, body, side):
        temp_turtles = []
        if side == "r":
            x_pos = 350
            y_pos = 40
            for i in body:
                i.setx(x_pos)
                i.sety(y_pos)
                i.showturtle()
                y_pos -= 20
                temp_turtles.append(i)
            return temp_turtles[:]
        else:
            x_pos = -350
            y_pos = 40
            for i in body:
                i.setx(x_pos)
                i.sety(y_pos)
                i.showturtle()
                y_pos -= 20
                temp_turtles.append(i)
            return temp_turtles[:]

    def move_up(self):
        for i in self.body:
            if i.pos()[1] >= 285:
                break
            else:
                i.sety(i.pos()[1] + self.move_pace)

    def move_down(self):
        for i in range(4, -1, -1):
            if self.body[i].pos()[1] <= -270:
                break
            else:
                self.body[i].sety(self.body[i].pos()[1] - self.move_pace)

    def reset_pos(self, side):
        for i in self.body:
            i.hideturtle()
        self.body = self.create_body(side)