import random
from turtle import Turtle
from setup import PadA
from player2 import PadB
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball_location = []
        self.balls = []
        self.angels_left_down = [290, 300, 310, 320, 330, 340]
        self.angels_left_up = [20, 30, 40, 50, 60, 70]
        self.angels_right_up = [110, 120, 130, 140, 150, 160]
        self.angels_right_down = [200, 210, 220, 230, 240, 250]

        ball = Turtle("circle")
        ball.shapesize(1)
        ball.penup()
        ball.color("white")
        ball.setheading(random.randrange(30, 350, 20))
        self.balls.append(ball)

    def ball_move(self, inv_A, inv_B):
        ab = 10
        #pad_b = PadB()
        #inventory_a = pad_a.paddle_inventory
        #inventory_b = pad_b.paddle_inventory
        while True:
            #time.sleep(0.0000001)
        #self.balls[0].setheading(270)
            #print(self.balls[0].distance(inv_A[0].pos()))
            self.balls[0].fd(20)
            x = self.balls[0].xcor()
            y = self.balls[0].ycor()
            if 280 < y < 300: #and y > 298:
                if 90 < self.balls[0].heading() < 180:
                    self.balls[0].setheading(self.angels_right_down[random.randrange(0, 6)])
                elif 0 < self.balls[0].heading() < 90:
                    self.balls[0].setheading(self.angels_left_down[random.randrange(0, 6)])
            elif -280 > y > -300:
                if 180 < self.balls[0].heading() < 270:
                    self.balls[0].setheading(self.angels_right_up[random.randrange(0, 6)])
                elif 270 < self.balls[0].heading() < 360:
                    self.balls[0].setheading(self.angels_left_up[random.randrange(0, 6)])

            elif self.balls[0].distance(inv_A[0].pos()) < 20 or self.balls[0].distance(inv_A[2].pos()) < 20 or \
                    self.balls[0].distance(inv_A[1].pos()) < 20 or self.balls[0].distance(inv_A[3].pos()) < 20: # Paddle Hit right
                if y > 10:
                    self.balls[0].setheading(self.angels_left_up[random.randrange(0, 6)])
                elif y < -10:
                    self.balls[0].setheading(self.angels_left_down[random.randrange(0, 6)])

            elif self.balls[0].distance(inv_B[0].pos()) < 20 or self.balls[0].distance(inv_B[2].pos()) < 20 or \
                    self.balls[0].distance(inv_B[1].pos()) < 20 or self.balls[0].distance(inv_B[3].pos()) < 20: # Paddle Hit left
                if y > 10:
                    self.balls[0].setheading(self.angels_right_up[random.randrange(0, 6)])
                elif y < -10:
                    self.balls[0].setheading(self.angels_right_down[random.randrange(0, 6)])

            elif -380 > x > -400: # Score and goal hits | Score Y
                self.balls[0].goto(0, 0)
                self.balls[0].setheading(random.randrange(30, 350, 20))
                return 2

            elif 380 < x < 400: # Score and goal hits | Score X
                self.balls[0].goto(0, 0)
                self.balls[0].setheading(random.randrange(30, 350, 20))
                return 3

            return 1
        #if ab == 0:
            #break
