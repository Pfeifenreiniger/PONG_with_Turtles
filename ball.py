
from turtle import Turtle
import random

LEFT_BORDER = -380
RIGHT_BORDER = 380
UPPER_BORDER = 280
LOWER_BORDER = -280

class Ball:
    def __init__(self):
        self.body = self.create_turtle()
        self.serve = False
        self.direct_hor = ""
        self.direct_ver = ""
        self.x_pos = 0
        self.y_pos = 0
        self.angle = 0
        self.rot_direct = random.randint(0, 1)
        self.move_pace = 15
        self.hit_by_paddle_l = False
        self.hit_by_paddle_r = False
        self.lost_for_paddle_l = False
        self.lost_for_paddle_r = False

    def create_turtle(self):
        tim = Turtle()
        tim.shape("turtle")
        tim.speed("fastest")
        tim.color("white")
        tim.penup()
        return tim

    def move(self):

        # serve
        if self.serve != True:
            serve_direct_hor = random.randint(0, 1)
            serve_direct_ver = random.randint(0, 1)
            if serve_direct_hor == 0:
                self.direct_hor = "left"
                if serve_direct_ver == 0:
                    self.direct_ver = "up"
                else:
                    self.direct_ver = "down"
                self.serve = True
            else:
                self.direct_hor = "right"
                if serve_direct_ver == 0:
                    self.direct_ver = "up"
                else:
                    self.direct_ver = "down"
                self.serve = True

        if self.serve:
            # moving left
            if self.direct_hor == "left":
                if self.x_pos > LEFT_BORDER and self.hit_by_paddle_l != True:
                    self.x_pos -= self.move_pace
                else:
                    if self.x_pos <= LEFT_BORDER:
                        self.lost_for_paddle_l = True
                    self.direct_hor = "right"
                    self.hit_by_paddle_l = False

            # moving right
            if self.direct_hor == "right":
                if self.x_pos < RIGHT_BORDER and self.hit_by_paddle_r != True:
                    self.x_pos += self.move_pace
                else:
                    if self.x_pos >= RIGHT_BORDER:
                        self.lost_for_paddle_r = True
                    self.direct_hor = "left"
                    self.hit_by_paddle_r = False

            # moving up
            if self.direct_ver == "up":
                if self.y_pos < UPPER_BORDER:
                    self.y_pos += self.move_pace
                else:
                    self.direct_ver = "down"

            # moving down
            if self.direct_ver == "down":
                if self.y_pos > LOWER_BORDER:
                    self.y_pos -= self.move_pace
                else:
                    self.direct_ver = "up"

        self.body.setx(self.x_pos)
        self.body.sety(self.y_pos)
        self.turtle_rotation()

    def turtle_rotation(self):
        self.body.setheading(self.angle)
        if self.rot_direct == 0:            # left around
            if self.angle + 10 > 350:
                self.angle = 0
            else:
                self.angle += 10
        else:                               # right around
            if self.angle - 10 < 0:
                self.angle = 350
            else:
                self.angle -= 10