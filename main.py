from turtle import Turtle, Screen
from setup import PadA
from player2 import PadB
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
player_1 = PadA()
player_1.paddle_a()
inventory_a = player_1.paddle_inventory
print(inventory_a)
player_2 = PadB()
player_2.paddle_b()
inventory_b = player_2.paddle_inventory
print(inventory_b)
ball = Ball()
screen.listen()
score_X = 0
score_Y = 0
score_x = Score().score_x()
score_y = Score().score_y()
font_a = ("Arial", 18, "normal")
screen.onkey(key="w", fun=player_1.move_up)
screen.onkey(key="s", fun=player_1.move_down)
screen.onkey(key="o", fun=player_2.move_up)
screen.onkey(key="k", fun=player_2.move_down)

while True:
    time.sleep(0.1)
    x = ball.ball_move(inv_A=inventory_a, inv_B=inventory_b)
    if x == 2:
        score_X += 1
        score_y.clear()
        score_y.write(f"Score B: {score_X}", align="center", font=font_a)
    elif x == 3:
        score_Y += 1
        score_x.clear()
        score_x.write(f"Score A: {score_Y}", align="center", font=font_a)
    if x >= 1:
        screen.update()
#screen.update()














screen.exitonclick()